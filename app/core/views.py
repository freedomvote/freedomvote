from django.shortcuts import render, get_object_or_404
from core.models import Politician, Question, State, Party, Answer, Statistic, Category
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json


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
            if request.POST.get('remove_image', None):
                politician.image = None
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
            politician = get_object_or_404(Politician, unique_url=request.POST['unique_url'])
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
    politician_list = Politician.objects.filter(statistic__id__gt=0).distinct()

    states          = State.objects.all().order_by('name')
    categories      = Category.objects.all().order_by('name')

    category = request.GET.get('category', None)
    state    = request.GET.get('state', None)
    search   = request.GET.get('search', None)

    per_site = request.GET.get('per_page', 10)
    page     = request.GET.get('page',      1)

    if category and category != '0':
        politician_list = Politician.objects.filter(statistic__category__id=category).order_by('-statistic__value')

    if state and state != '0':
        politician_list = politician_list.filter(state=state)

    if search:
        politician_list = politician_list.filter(
            Q(last_name__icontains=search) |
            Q(first_name__icontains=search) |
            Q(state__name__icontains=search) |
            Q(party__name__icontains=search) |
            Q(party__shortname__icontains=search)
        )

    paginator = Paginator(politician_list, per_site)

    try:
        politicians = paginator.page(page)
    except PageNotAnInteger:
        politicians = paginator.page(1)
    except EmptyPage:
        politicians = paginator.page(paginator.num_pages)

    # remove the page parameter from url
    request.GET = request.GET.copy()
    if request.GET.get('page', None):
        request.GET.pop('page')

    return render(
        request,
        'core/citizen.html',
        {
            'politicians' : politicians,
            'categories'  : categories,
            'states'      : states,
        }
    )

def calculate_statistic_view(request, unique_url):
    politician = get_object_or_404(Politician, unique_url=unique_url)
    categories = Category.objects.all()

    for category in categories:
        answers = Answer.objects.filter(question__category=category, politician=politician)
        if answers:
            diffs = []
            for answer in answers:
                diffs.append(abs(answer.question.preferred_answer - answer.agreement_level))

            diff = 10 - sum(diffs) / float(len(diffs))

            stat, created = Statistic.objects.get_or_create(
                politician=politician,
                category=category,
                defaults={'value': diff}
            )
            stat.value = diff
            stat.save()

    return HttpResponseRedirect('/parlamentarier/%s' % unique_url)


def retract_statistic_view(request, unique_url):
    politician = get_object_or_404(Politician, unique_url=unique_url)
    Statistic.objects.filter(politician=politician).delete()

    return HttpResponseRedirect('/parlamentarier/%s' % unique_url)

def statistic_view(request, politician_id):
    statistics = Statistic.objects.filter(politician__id=politician_id)

    categories = [s.category.name for s in statistics]
    values     = [s.value for s in statistics]

    response = {
        'categories' : categories,
        'values'     : values
    }

    return HttpResponse(json.dumps(response), content_type="application/json")


def detail_view(request, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)
    answers    = Answer.objects.filter(politician=politician).order_by('question__question_number')

    return render(
        request,
        'core/detail.html',
        {
            'politician' : politician,
            'answers'    : answers
        }
    )
