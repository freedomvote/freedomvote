from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from colorfield.fields import ColorField
import base64
import os


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
        ordering            = ['name']


class Party(models.Model):
    name                    = models.CharField(
        max_length          = 50,
        verbose_name        = _('name')
    )
    shortname               = models.CharField(
        max_length          = 10,
        verbose_name        = _('shortname')
    )
    background_color        = ColorField(
        default             = '#3F51B5',
        verbose_name        = _('background_color')
    )
    font_color              = ColorField(
        default             = '#FFFFFF',
        verbose_name        = _('font_color')
    )

    def __unicode__(self):
        return self.shortname

    class Meta:
        verbose_name        = _('party')
        verbose_name_plural = _('parties')
        ordering            = ['name']


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
    user                    = models.ForeignKey(
        User,
        verbose_name        = _('user')
    )
    first_name              = models.CharField(
        max_length          = 100,
        blank               = True,
        null                = True,
        verbose_name        = _('first_name')
    )
    last_name               = models.CharField(
        max_length          = 100,
        blank               = True,
        null                = True,
        verbose_name        = _('last_name')
    )
    email                   = models.EmailField(
        blank               = True,
        null                = True,
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
    unique_key              = models.CharField(
        max_length          = 20,
        verbose_name        = _('unique_key'),
        default             = generate_url
    )
    state                   = models.ManyToManyField(
        State,
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
    is_active               = models.BooleanField(
        default             = True,
        verbose_name        = _('is_active')
    )

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @classmethod
    def get_politicians_by_category(cls, category_id, input_value, order='-accordance'):
        return cls.objects.filter(statistic__category_id=category_id).extra(
            select={'accordance':'core_statistic_compare(value::integer, %d::integer)' % input_value}
        ).order_by(order)

    @property
    def party_name(self):
        if self.party:
            return self.party.name
        elif self.party_other:
            return self.party_other
        else:
            return '-'

    @property
    def party_short(self):
        if self.party:
            return self.party.shortname
        elif self.party_other:
            return self.party_other
        else:
            return '-'

    @property
    def state_name(self):
        state_count = self.state.count()
        if state_count > 1:
            return _('%s states') % state_count
        elif state_count == 1:
            return self.state.first().name
        else:
            return '-'

    def get_details(self):
        if not self.party and not self.state:
            return ''
        elif self.party and not self.state:
            return '(%s)' % self.party_short
        elif not self.party and self.state:
            return '(%s)' % self.state_name
        else:
            return '(%s, %s)' % (self.state_name, self.party_short)

    @property
    def unique_url(self):
        return '%s%s' % (
            settings.BASE_URL,
            reverse('politician_edit', args=[self.unique_key])
        )

    class Meta:
        verbose_name        = _('politician')
        verbose_name_plural = _('politicians')


class Link(models.Model):
    politician              = models.ForeignKey(
        Politician,
        verbose_name        = _('politician')
    )
    url                     = models.URLField(
        verbose_name        = _('url')
    )

    class Meta:
        verbose_name        = _('link')
        verbose_name_plural = _('links')


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
    description             = models.TextField(
        null                = True,
        blank               = True,
        verbose_name        = _('description')
    )

    class Meta:
        verbose_name        = _('question')
        verbose_name_plural = _('questions')
        ordering            = ['category__name']


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
    value                   = models.IntegerField(
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
            GROUP BY s.id, q.category_id, c.name
            ORDER BY c.name
        ''', [politician_id])

    class Meta:
        verbose_name        = _('statistic')
        verbose_name_plural = _('statistics')


class RegistrationKey(models.Model):
    user                    = models.OneToOneField(
        User,
        on_delete           = models.CASCADE
    )
    unique_key              = models.CharField(
        max_length          = 20,
        verbose_name        = _('unique_key'),
        default             = generate_url
    )


@receiver(post_save, sender=User)
def create_user_registration_key(sender, instance, created, **kwargs):
    if created:
        RegistrationKey.objects.create(user=instance)
