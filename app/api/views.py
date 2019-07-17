from core.models import Politician, Question, Statistic, Answer, Category
from django.http import JsonResponse
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from api import util, serializers
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


def v1(request):
    questions = [
        {
            'id': x.id,
            'category_id': x.category.id,
            'text': util.get_model_translations(x, 'text'),
            'description': util.get_model_translations(x, 'description'),
            'preferred_answer': x.preferred_answer
        }
        for x
        in Question.objects.all().order_by('id')
    ]

    categories = [
        {
            'id': x.id,
            'name': util.get_model_translations(x, 'name'),
        }
        for x
        in Category.objects.all().order_by('id')
    ]

    politicians = []

    for x in Politician.objects.all().order_by('id'):
        if Statistic.objects.filter(politician=x).exists():
            p = {
                'id':                      x.id,
                'first_name':              x.first_name if x.first_name else None,
                'last_name':               x.last_name if x.last_name else None,
                'is_member_of_parliament': x.is_member_of_parliament,
                'image':                   x.image.url if x.image else None,
                'state':                   x.state.name if x.state.name else None,
                'past_contributions':      x.past_contributions,
                'future_plans':            x.future_plans,
                'answers':                 []
            }

            if x.party:
                p['party'] = {
                        'name':      x.party.name,
                        'shortname': x.party.shortname
                }
            elif x.party_other:
                p['party']= {
                    'name':      x.party_other,
                    'shortname': None
                }
            else:
                p['party'] = None

            for a in Answer.objects.filter(politician=x).order_by('id'):
                p['answers'].append({
                    'question_id': a.question.id,
                    'answer': a.agreement_level,
                    'note': a.note
                })

            politicians.append(p)

    return JsonResponse({ 'politicians': politicians, 'questions': questions, 'categories': categories })


class PoliticianViewSet(ReadOnlyModelViewSet):
    queryset = Politician.objects.filter(statistic__id__gt=0).distinct()
    serializer_class = serializers.PoliticianSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filter_fields = ('state','party','is_member_of_parliament')
    search_fields = (
        'first_name',
        'last_name',
        'state__name',
        'party__name',
        'party__shortname',
        'party_other'
    )
