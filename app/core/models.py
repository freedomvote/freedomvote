from django.db import models
import os
import base64
from django.utils.translation import ugettext_lazy as _

def generate_url():
    key = base64.urlsafe_b64encode(os.urandom(16))[:20]
    return key

class State(models.Model):
    name                    = models.CharField(
        max_length          = 50,
        verbose_name        = _('name')
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = _('state')
        verbose_name_plural = _('states')


class Party(models.Model):
    name                    = models.CharField(
        max_length          = 50,
        verbose_name        = _('name')
    )
    shortname               = models.CharField(
        max_length          = 10,
        verbose_name        = _('shortname')
    )

    def __unicode__(self):
        return self.shortname

    class Meta:
        verbose_name        = _('party')
        verbose_name_plural = _('parties')


class Category(models.Model):
    name                    = models.CharField(
        max_length          = 50,
        verbose_name        = _('name')
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = _('category')
        verbose_name_plural = _('categories')


class Politician(models.Model):
    first_name              = models.CharField(
        max_length          = 100,
        verbose_name        = _('first_name')
    )
    last_name               = models.CharField(
        max_length          = 100,
        verbose_name        = _('last_name')
    )
    email                   = models.EmailField(
        verbose_name        = _('email')
    )
    image                   = models.ImageField(
        upload_to           = 'politicians/',
        null                = True,
        blank               = True,
        verbose_name        = _('image')
    )
    is_member_of_parliament = models.BooleanField(
        default             = False,
        verbose_name        = _('is_member_of_parliament')
    )
    past_contributions      = models.TextField(
        blank               = True,
        verbose_name        = _('past_contributions')
    )
    future_plans            = models.TextField(
        blank               = True,
        verbose_name        = _('future_plans')
    )
    unique_url              = models.CharField(
        max_length          = 20,
        verbose_name        = _('unique_url'),
        default             = generate_url
    )
    state                   = models.ForeignKey(
        State,
        null                = True,
        blank               = True,
        verbose_name        = _('state')
    )
    party                   = models.ForeignKey(
        Party,
        null                = True,
        blank               = True,
        verbose_name        = _('party')
    )
    party_other             = models.CharField(
        max_length          = 50,
        null                = True,
        blank               = True,
        verbose_name        = _('party_other')
    )

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @classmethod
    def get_politicians_by_category(cls, category_id, input_value, order='-accordance'):
        return cls.objects.filter(statistic__category_id=category_id).extra(
            select={'accordance':'core_statistic_compare(value::integer, %d::integer)' % input_value}
        ).order_by(order)

    @property
    def get_party(self):
        if self.party:
            return self.party.name
        elif self.party_other:
            return self.party_other
        else:
            return '-'

    @property
    def get_state(self):
        if self.state:
            return self.state.name
        else:
            return '-'

    class Meta:
        verbose_name        = _('politician')
        verbose_name_plural = _('politicians')


class Question(models.Model):
    preferred_answer        = models.IntegerField(
        verbose_name        = _('preferred_answer')
    )
    question_number         = models.IntegerField(
        verbose_name        = _('question_number')
    )
    category                = models.ForeignKey(
        Category,
        verbose_name        = _('category')
    )
    text                    = models.TextField(
        verbose_name        = _('text')
    )

    class Meta:
        verbose_name        = _('question')
        verbose_name_plural = _('questions')


class Answer(models.Model):
    question                = models.ForeignKey(
        Question,
        verbose_name        = _('question')
    )
    politician              = models.ForeignKey(
        Politician,
        verbose_name        = _('politician')
    )
    agreement_level         = models.IntegerField(
        verbose_name        = _('agreement_level')
    )
    note                    = models.TextField(
        verbose_name        = _('note')
    )

    class Meta:
        verbose_name        = _('answer')
        verbose_name_plural = _('answers')


class Statistic(models.Model):
    politician              = models.ForeignKey(
        Politician,
        verbose_name        = _('politician')
    )
    category                = models.ForeignKey(
        Category,
        verbose_name        = _('category')
    )
    value                   = models.FloatField(
        verbose_name        = _('value')
    )

    @classmethod
    def get_accordance(cls, politician_id, category_id, input_value):
        statistic = cls.objects.filter(politician_id=politician_id, category_id=category_id).extra(
            select={
                'accordance' : 'core_statistic_compare(value::integer, %d::integer)' % input_value
            }
        ).first()

        return (statistic.accordance if statistic else 0)

    @classmethod
    def get_statistics_by_politician(cls, politician_id):
        return cls.objects.raw('''
            SELECT
                s.*,
                core_statistic_compare(s.value::integer, AVG(q.preferred_answer*10)::integer) AS accordance
            FROM core_statistic AS s
            JOIN core_category AS c ON (
                s.category_id = c.id
            )
            JOIN core_question AS q ON (
                c.id = q.category_id
            )
            WHERE s.politician_id = %s
            GROUP BY s.id, q.category_id
        ''', [politician_id])

    class Meta:
        verbose_name        = _('statistic')
        verbose_name_plural = _('statistics')
