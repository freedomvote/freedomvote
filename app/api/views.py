from core.models import Politician, Question, Statistic, Answer
from django.http import JsonResponse
from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder

def v1(request):
    questions = [
        {
            'id': x.id,
            'text': {
                'de': x.text_de if x.text_de else '',
                'fr': x.text_fr if x.text_fr else '',
                'it': x.text_it if x.text_it else ''
            },
            'description': {
                'de': x.description_de if x.description_de else '',
                'fr': x.description_fr if x.description_fr else '',
                'it': x.description_it if x.description_it else ''
            }
        }
        for x
        in Question.objects.all().order_by('id')
    ]

    politicians = []

    for x in Politician.objects.all().order_by('id'):
        if Statistic.objects.filter(politician=x).exists():
            p = {
                'id':                      x.id,
                'first_name':              x.first_name if x.image else None,
                'last_name':               x.last_name if x.image else None,
                'is_member_of_parliament': x.is_member_of_parliament,
                'image':                   x.image.url if x.image else None,
                'state':                   x.state.name if x.state else None,
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

    return JsonResponse({ 'politicians': politicians, 'questions': questions })

