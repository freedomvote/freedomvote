from django.shortcuts import render, get_object_or_404
from core.models import Politician, Question, State, Party, Answer
from django.http import HttpResponse


def politician_view(request, unique_url):
    politician = get_object_or_404(Politician, unique_url=unique_url)
    questions  = Question.objects.all().order_by('question_number')
    answers    = Answer.objects.filter(politician=politician)
    states     = State.objects.all().order_by('name')
    parties    = Party.objects.all().order_by('name')

    if request.POST:
        try:
            politician.email = request.POST['email']
            politician.future_plans = request.POST['future_plans']
            politician.past_contributions = request.POST['past_contributions']
            politician.is_member_of_parliament = bool(request.POST.get('is_member_of_parliament', False))
            print(politician.is_member_of_parliament)
            print(bool(request.POST.get('is_member_of_parliament', False)) )
            politician.party_other = request.POST['party_other']
            try:
                politician.image = request.FILES['image']
            except:
                pass
            try:
                politician.state = State.objects.get(id=request.POST['state'])
            except:
                politician.state = None
            try:
                politician.party = Party.objects.get(id=request.POST['party'])
            except:
                politician.party = None
            politician.save()

        except:
            pass

    return render(
        request,
        'core/politician.html',
        {
            'politician' : politician,
            'questions'  : questions,
            'answers'    : answers,
            'states'     : states,
            'parties'    : parties,
        }
    )

def answer_view(request):
    if request.POST:
        try:
            question = get_object_or_404(Question, pk=request.POST['question'])
            politician = get_object_or_404(Politician, pk=request.POST['politician'])
            try:
                answer = Answer.objects.get(
                    question=question,
                    politician=politician
                )
            except:
                answer = Answer(
                    question=question,
                    politician=politician
                )
            answer.agreement_level = request.POST.get('agreement_level', 0)
            answer.note = request.POST['note']
            answer.save()
        except:
            pass

    return HttpResponse('')

def citizen_view(request):
    politicians = Politician.objects.all()

    return render(
        request,
        'core/citizen.html',
        {
            'politicians' : politicians,
        }
    )
