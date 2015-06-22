from core.decorators import require_party_login
from core.forms import PoliticianForm, PartyPoliticianForm
from core.models import Politician, Question, State, Answer, Statistic, Category, LinkType, Link
from core.tools import set_cookie, get_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.db.models import Q, Sum
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
import csv
import re

##
# ERROR VIEWS
##

def handler404(request):
    response = render(request, '404.html')
    response.status_code = 404

    return response


def handler500(request):
    response = render(request, '500.html')
    response.status_code = 500

    return response

##
# PUBLIC VIEWS
##

def candidates_view(request):
    politician_list = Politician.objects.filter(statistic__id__gt=0).distinct()

    states          = State.objects.all().order_by('name')
    categories      = Category.objects.filter(statistic__id__gt=0).order_by('name').distinct()

    category = request.GET.get('category', None)
    state    = request.GET.get('state', None)
    search   = request.GET.get('search', None)

    per_site = request.GET.get('per_page', 10)
    page     = request.GET.get('page',      1)


    request.GET = request.GET.copy()
    if request.GET.has_key('evaluate') and get_cookie(request, 'statistics', {}) == {}:
        request.GET.pop('evaluate')

    if category and category != '0':
        if request.GET.has_key('evaluate'):
            stats = get_cookie(request, 'statistics', {})
            val = stats.get('category_%s' % category, 0)
        else:
            val = Question.objects.filter(
                category__id=category
            ).aggregate(Sum('preferred_answer'))['preferred_answer__sum']

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
    if request.GET.get('page', None):
        request.GET.pop('page')

    return render(
        request,
        'core/candidates/index.html',
        {
            'politicians' : politicians,
            'categories'  : categories,
            'states'      : states,
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
                values.append(
                    abs(
                        question.preferred_answer -
                        int(session_answers.get('question_%d' % question.id, 0))
                    )
                )
                session_statistics['category_%d' % category.id] = 10 - sum(values) / float(len(cq))

        request.COOKIES['answers'] = session_answers
        request.COOKIES['statistics'] = session_statistics
        messages.success(request, _('answers_saved_successfully_evaluate'))

    for question in questions:
        item = {
            'question' : question,
            'value'    : session_answers.get('question_%d' % question.id, 0)
        }
        data.append(item)

    response = render(
        request,
        'core/compare/index.html',
        {
            'data' : data
        }
    )

    set_cookie(response, 'answers', session_answers, 30)
    set_cookie(response, 'statistics', session_statistics, 30)

    return response

def compare_reset_view(request):
    messages.success(request, _('answers_resetted'))

    response = HttpResponseRedirect(reverse('compare'))

    set_cookie(response, 'answers', {}, 30)
    set_cookie(response, 'statistics', {}, 30)

    return response

##
# PRIVATE POLITICIAN VIEWS
##

def politician_edit_view(request, unique_key):
    return redirect(reverse('politician_edit_profile', args=[unique_key]))

def politician_edit_profile_view(request, unique_key):
    politician = get_object_or_404(Politician, unique_key=unique_key)
    link_types = LinkType.objects.all().order_by('name')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

    if request.POST:
        form = PoliticianForm(request.POST, request.FILES, instance=politician)
        if form.is_valid():
            form.save()
            messages.success(request, _('profile_saved_successfully'))
    else:
        form = PoliticianForm(instance=politician)

    return render(
        request,
        'core/edit/profile.html',
        {
            'politician' : politician,
            'form'       : form,
            'link_types' : link_types,
            'links'      : links
        }
    )

def politician_edit_questions_view(request, unique_key):
    politician = get_object_or_404(Politician, unique_key=unique_key)
    questions  = Question.objects.all().order_by('question_number')
    answers    = Answer.objects.filter(politician=politician)

    return render(
        request,
        'core/edit/questions.html',
        {
            'politician' : politician,
            'questions'  : questions,
            'answers'    : answers
        }
    )

def politician_answer_view(request, unique_key):
    if request.POST:
        question = get_object_or_404(Question, id=request.POST.get('question'))
        politician = get_object_or_404(Politician, unique_key=unique_key)
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

def politician_publish_view(request, unique_key):
    politician = get_object_or_404(Politician, unique_key=unique_key)
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

    return JsonResponse({
        'type': 'success',
        'text': force_unicode(_('answers_published_successfully'))
    })


def politician_unpublish_view(request, unique_key):
    politician = get_object_or_404(Politician, unique_key=unique_key)
    Statistic.objects.filter(politician=politician).delete()

    return JsonResponse({
        'type': 'success',
        'text': force_unicode(_('answers_unpublished_successfully'))
    })

def politician_link_add_view(request, unique_key):
    politician = get_object_or_404(Politician, unique_key=unique_key)
    link_type  = get_object_or_404(LinkType, id=request.POST.get('link_type'))
    url        = request.POST.get('url')
    error      = False

    if url.startswith(('http://', 'https://')) and '.' in url:
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

    return render(request, 'core/edit/links.html', {
        'links'      : links,
        'link_types' : types,
        'politician' : politician,
        'error'      : error,
        'input'      : url,
        'link_type'  : link_type,
    })

def politician_link_delete_view(request, unique_key, link_id):
    politician = get_object_or_404(Politician, unique_key=unique_key)
    link = get_object_or_404(Link, id=link_id)
    link.delete()

    types      = LinkType.objects.all().order_by('name')
    links      = Link.objects.filter(politician=politician).order_by('type__name')

    return render(request, 'core/edit/links.html', {
        'links'      : links,
        'link_types' : types,
        'politician' : politician
    })

##
# PUBLIC POLITICIAN VIEWS
##

def politician_view(request, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)
    answers    = Answer.objects.filter(politician=politician).order_by('question__question_number')
    links      = Link.objects.filter(politician=politician).order_by('type__name')
    cookie     = get_cookie(request, 'answers', {})
    answer_obs = []

    for a in answers:
        answer_obs.append({
            'own_ans': cookie.get('question_%s' % a.question.id, None),
            'politician_ans': a
        })

    return render(
        request,
        'core/profile/index.html',
        {
            'politician' : politician,
            'answers'    : answer_obs,
            'links'      : links
        }
    )

def politician_statistic_view(request, politician_id):
    statistics = Statistic.get_statistics_by_politician(politician_id)

    category_list = [s.category.name for s in statistics]
    if request.GET.has_key('compare'):
        stats = get_cookie(request, 'statistics', {})
        value_list = {
            'politician' : [s.accordance for s in statistics],
            'citizen'    : [stats.get('category_%d' % s.category.id, 0) for s in statistics]
        }
    elif request.GET.has_key('evaluate'):
        pairs = []
        statistics    = get_cookie(request, 'statistics', {})
        for k, v in statistics.iteritems():
            category_id = int(re.sub('category_', '', k))
            pairs.append({
                'category': Category.objects.get(id=category_id).name,
                'value':    Statistic.get_accordance(politician_id, category_id, (int(v)*10))
            })

        sorted_pairs = sorted(pairs, key=lambda k: k['category'])
        value_list = [i['value'] for i in sorted_pairs]
        category_list = [i['category'] for i in sorted_pairs]

    else:
        value_list = [s.accordance for s in statistics]

    response = {
        'categories' : category_list,
        'values'     : value_list
    }

    return JsonResponse(response)

##
# PARTY VIEWS
##

def party_login_view(request, party_name):
    user = get_object_or_404(User, username=party_name)

    if request.user.is_authenticated() and request.user.username == party_name:
        return redirect(reverse('party_dashboard', args=[party_name]))

    if request.POST:
        user = authenticate(username=party_name, password=request.POST.get('password'))
        if user and user.is_active:
            login(request, user)
            messages.success(request, _('login_successful'))
            return redirect(reverse('party_dashboard', args=[party_name]))
        else:
            messages.error(request, _('login_error'))

    return render(request, 'core/party/login.html')

def party_logout_view(request, party_name):
    logout(request)

    return redirect(reverse('party_login', args=[party_name]))

@require_party_login
def party_dashboard_view(request, party_name):
    return render(
        request,
        'core/party/dashboard.html',
        {
            'politicians': Politician.objects.filter(user=request.user)
        }
    )

@require_party_login
def party_politician_add_view(request, party_name):
    if request.POST:
        form = PartyPoliticianForm(request.POST, request.FILES)
        form.data['user'] = request.user.id
        if form.is_valid():
            form.save()
            messages.success(request, _('politician_add_success'))
            return redirect(reverse('party_dashboard', args=[party_name]))
        else:
            messages.error(request, _('politician_add_error'))

    else:
        form = PartyPoliticianForm()

    return render(
        request,
        'core/party/politician_edit.html',
        {
            'politician' : None,
            'form'       : form
        }
    )

@require_party_login
def party_politician_edit_view(request, party_name, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)

    if request.POST:
        form = PartyPoliticianForm(request.POST, request.FILES, instance=politician)
        form.data['user'] = request.user.id
        if form.is_valid():
            form.save()
            messages.success(request, _('politician_edit_success'))
            return redirect(reverse('party_dashboard', args=[party_name]))
        else:
            messages.error(request, _('politician_edit_error'))

    else:
        form = PartyPoliticianForm(instance=politician)

    return render(
        request,
        'core/party/politician_edit.html',
        {
            'politician' : None,
            'form'       : form
        }
    )
    pass

@require_party_login
def party_export_view(request, party_name):
    politicians = Politician.objects.filter(user=request.user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="freedomvote_export.csv"'

    writer = csv.writer(response)
    writer.writerow([
        force_unicode(_('first_name')),
        force_unicode(_('last_name')),
        force_unicode(_('state')),
        force_unicode(_('unique_url'))
    ])

    for p in politicians:
        writer.writerow([p.first_name, p.last_name, p.state, p.unique_url])

    return response

@require_party_login
def party_politician_delete_view(request, party_name, politician_id):
    politician = get_object_or_404(Politician, id=politician_id)
    politician.delete()
    messages.success(request, _('politician_delete_success') % (politician.first_name, politician.last_name))

    return redirect(reverse('party_dashboard', args=[party_name]))
