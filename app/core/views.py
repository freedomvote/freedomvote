from core.models import Politician, Question, State, Party, Answer, Statistic, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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

def politician_answer_view(request):
    if request.POST:
        question = get_object_or_404(Question, pk=request.POST.get('question'))
        politician = get_object_or_404(Politician, unique_url=request.POST.get('unique_url'))
        answer, created = Answer.objects.get_or_create(
            question=question,
            politician=politician,
            defaults={
                'agreement_level' : request.POST.get('agreement_level', 0)
            }
        )
        answer.agreement_level = request.POST.get('agreement_level', 0)
        answer.note = request.POST['note']
        answer.save()

    return HttpResponse('')

def search_view(request):
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
        'core/search.html',
        {
            'politicians' : politicians,
            'categories'  : categories,
            'states'      : states,
        }
    )

def publish_view(request):
    unique_url = request.POST.get('unique_url')
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

    return HttpResponseRedirect(reverse('politician', args=[unique_url]))


def unpublish_view(request):
    unique_url = request.POST.get('unique_url')
    politician = get_object_or_404(Politician, unique_url=unique_url)
    Statistic.objects.filter(politician=politician).delete()

    return HttpResponseRedirect(reverse('politician', args=[unique_url]))

def profile_info_view(request, politician_id):
    statistics = Statistic.objects.filter(politician__id=politician_id)

    categories = [s.category.name for s in statistics]
    if not request.GET.get('compare', False):
        values = [s.value for s in statistics]
    else:
        stats = request.session.get('statistics', {})
        values = {
            'politician' : [s.value for s in statistics],
            'citizen'    : [stats.get('category_%d' % s.category.id, 0) for s in statistics]
        }



    response = {
        'categories' : categories,
        'values'     : values
    }

    return HttpResponse(json.dumps(response), content_type="application/json")


def profile_view(request, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)
    answers    = Answer.objects.filter(politician=politician).order_by('question__question_number')

    return render(
        request,
        'core/profile.html',
        {
            'politician' : politician,
            'answers'    : answers
        }
    )

def compare_view(request):
    questions = Question.objects.all()
    data      = []
    if not request.session.has_key('answers'):
        request.session['answers'] = {}
    if not request.session.has_key('statistics'):
        request.session['statistics'] = {}

    if request.POST:
        for question in questions:
            qid = 'question_%d' % question.id
            request.session['answers'][qid] = request.POST.get(qid,0)

        categories = Category.objects.all()

        for category in categories:
            cq = Question.objects.filter(category=category)
            values = []
            for question in cq:
                values.append(abs(question.preferred_answer - int(request.session['answers'].get('question_%d' % question.id, 0))))
                request.session['statistics']['category_%d' % category.id] = 10 - sum(values) / float(len(cq))

        request.session.modified = True

    for question in questions:
        item = {
            'question' : question,
            'value'    : request.session['answers'].get('question_%d' % question.id, 0)
        }
        data.append(item)

    return render(
        request,
        'core/compare.html',
        {
            'data' : data
        }
    )
