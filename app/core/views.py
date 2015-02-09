from django.shortcuts import render
from core.models import Politician, Question, State, Party


def politician_view(request, unique_url):
    politician = Politician.objects.get(unique_url=unique_url)
    questions  = Question.objects.all().order_by('question_number')
    states     = State.objects.all().order_by('name')
    parties    = Party.objects.all().order_by('name')

    return render(
        request,
        'core/politician.html',
        {
            'politician' : politician,
            'questions'  : questions,
            'states'     : states,
            'parties'    : parties,
        }
    )

def politician_update_view(request):
    if request.POST:
        pass
