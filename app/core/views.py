from core.models import Politician, Question, State, Party, Answer, Statistic, Category, LinkType, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
import re
import datetime
from django.conf import settings


def politician_view(request, unique_url):
    politician = get_object_or_404(Politician, unique_url=unique_url)
    questions  = Question.objects.all().order_by('question_number')
    answers    = Answer.objects.filter(politician=politician)
    states     = State.objects.all().order_by('name')
    parties    = Party.objects.all().order_by('name')
    types      = LinkType.objects.all().order_by('name')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

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
            'types'      : types,
            'links'      : links,
        }
    )

def politician_answer_view(request):
    if request.POST:
        question = get_object_or_404(Question, pk=request.POST.get('question'))
        politician = get_object_or_404(Politician, unique_url=request.POST.get('unique_url'))
        agreement_level = int(request.POST.get('agreement_level', 0))

        answer, created = Answer.objects.get_or_create(
            question=question,
            politician=politician,
            defaults={
                'agreement_level' : agreement_level,
            }
        )
        answer.agreement_level = agreement_level
        answer.note = request.POST['note']
        answer.save()

    return HttpResponse('')

def candidates_view(request):
    politician_list = Politician.objects.filter(statistic__id__gt=0).distinct()

    states          = State.objects.all().order_by('name')
    categories      = Category.objects.filter(statistic__id__gt=0).order_by('name').distinct()

    category = request.GET.get('category', None)
    state    = request.GET.get('state', None)
    search   = request.GET.get('search', None)

    per_site = request.GET.get('per_page', 10)
    page     = request.GET.get('page',      1)

    if category and category != '0':
        if request.GET.has_key('evaluate'):
            stats = get_cookie(request, 'statistics', {})
            val = stats.get('category_%s' % category, 0)
        else:
            val = Question.objects.filter(category__id=category).aggregate(Sum('preferred_answer'))['preferred_answer__sum']

        politician_list = Politician.get_politicians_by_category(category, (int(val)*10))

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
        'core/candidates.html',
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
            value = int(answers.aggregate(Sum('agreement_level'))['agreement_level__sum'] / answers.count() * 10)
            stat, created = Statistic.objects.get_or_create(
                politician=politician,
                category=category,
                defaults={'value': value}
            )
            stat.value = value
            stat.save()

    return HttpResponse('')


def unpublish_view(request):
    unique_url = request.POST.get('unique_url')
    politician = get_object_or_404(Politician, unique_url=unique_url)
    Statistic.objects.filter(politician=politician).delete()

    return HttpResponse('')

def profile_info_view(request, politician_id):
    statistics = Statistic.get_statistics_by_politician(politician_id)

    category_list = [s.category.name for s in statistics]
    if request.GET.has_key('compare'):
        stats = get_cookie(request, 'statistics', {})
        value_list = {
            'politician' : [s.accordance for s in statistics],
            'citizen'    : [stats.get('category_%d' % s.category.id, 0) for s in statistics]
        }
    elif request.GET.has_key('evaluate'):
        value_list    = []
        category_list = []
        statistics    = get_cookie(request, 'statistics', {})
        for k, v in statistics.iteritems():
            category_id = int(re.sub('category_', '', k))
            value_list.append(Statistic.get_accordance(politician_id, category_id, (int(v)*10)))
            category_list.append(Category.objects.get(id=category_id).name)

    else:
        value_list = [s.accordance for s in statistics]

    response = {
        'categories' : category_list,
        'values'     : value_list
    }

    return JsonResponse(response)


def profile_view(request, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)
    answers    = Answer.objects.filter(politician=politician).order_by('question__question_number')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

    return render(
        request,
        'core/profile.html',
        {
            'politician' : politician,
            'answers'    : answers,
            'links'      : links
        }
    )

def compare_view(request):
    questions = Question.objects.all()
    data      = []

    session_answers    = get_cookie(request, 'answers',    {})
    session_statistics = get_cookie(request, 'statistics', {})

    if request.POST:
        for question in questions:
            qid = 'question_%d' % question.id
            session_answers[qid] = request.POST.get(qid,0)

        categories = Category.objects.all()

        for category in categories:
            cq = Question.objects.filter(category=category)
            values = []
            for question in cq:
                values.append(abs(question.preferred_answer - int(session_answers.get('question_%d' % question.id, 0))))
                session_statistics['category_%d' % category.id] = 10 - sum(values) / float(len(cq))

        request.COOKIES['answers'] = session_answers
        request.COOKIES['statistics'] = session_statistics

    for question in questions:
        item = {
            'question' : question,
            'value'    : session_answers.get('question_%d' % question.id, 0)
        }
        data.append(item)

    response = render(
        request,
        'core/compare.html',
        {
            'data' : data
        }
    )

    set_cookie(response, 'answers', session_answers, 30)
    set_cookie(response, 'statistics', session_statistics, 30)

    return response


def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  #one year
    else:
        max_age = days_expire * 24 * 60 * 60
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
            '%a, %d-%b-%Y %H:%M:%S GMT'
        )
        response.set_cookie(
            key,
            json.dumps(value),
            max_age=max_age,
            expires=expires,
            domain=settings.SESSION_COOKIE_DOMAIN,
            secure=settings.SESSION_COOKIE_SECURE or None
        )

def get_cookie(request, key, default):
    strval = request.COOKIES.get(key)
    if strval:
        return json.loads(strval)
    return default

def add_link_view(request):
    politician = get_object_or_404(Politician, unique_url=request.POST.get('unique_url'))
    link_type  = get_object_or_404(LinkType, id=request.POST.get('link_type'))
    url        = request.POST.get('url')
    error      = False

    if url.startswith(('http://', 'https://')):
        l = Link(
            type=link_type,
            politician=politician,
            url=url
        )
        l.save()
        url = ''
    else:
        error = True

    types      = LinkType.objects.all().order_by('name')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

    return render(request, 'core/links.html', {
        'links' : links,
        'types' : types,
        'politician' : politician,
        'error' : error,
        'input' : url,
        'link_type' : link_type,
    })

def delete_link_view(request):
    politician = get_object_or_404(Politician, unique_url=request.POST.get('unique_url'))
    link = get_object_or_404(Link, id=request.POST.get('link_id'))
    link.delete()

    types      = LinkType.objects.all().order_by('name')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

    return render(request, 'core/links.html', {
        'links' : links,
        'types' : types,
        'politician' : politician
    })
