from django.conf.urls import patterns, url, include
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from core import views

urlpatterns = patterns(

    # public urls

    '',
    url(
        r'^i18n/',
        include('django.conf.urls.i18n')
    ),
    url(r'^candidates/$',
        cache_page(3600)(views.candidates_view),
        name='candidates'
    ),
    url(r'^compare/$',
        views.compare_view,
        name='compare'
    ),
    url(r'^compare/reset/$',
        views.compare_reset_view,
        name='compare_reset'
    ),
    url(r'^partners/$',
        cache_page(3600)(TemplateView.as_view(template_name='partners.html')),
        name='partners'
    ),

    # private politician urls

    url(r'^politician/(?P<unique_key>[^/]+)/edit/$',
        views.politician_edit_view,
        name='politician_edit'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/edit/profile/$',
        views.politician_edit_profile_view,
        name='politician_edit_profile'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/edit/questions/$',
        views.politician_edit_questions_view,
        name='politician_edit_questions'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/answer/$',
        views.politician_answer_view,
        name='politician_answer'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/publish/$',
        views.politician_publish_view,
        name='politician_publish'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/unpublish/$',
        views.politician_unpublish_view,
        name='politician_unpublish'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/link/add/$',
        views.politician_link_add_view,
        name='politician_link_add'
    ),
    url(r'^politician/(?P<unique_key>[^/]+)/link/(?P<link_id>\d+)/delete/$',
        views.politician_link_delete_view,
        name='politician_link_delete'
    ),

    # public politician urls

    url(r'^politician/(?P<politician_id>\d+)/$',
        cache_page(3600)(views.politician_view),
        name='politician'
    ),
    url(r'^politician/(?P<politician_id>\d+)/statistic/$',
        views.politician_statistic_view,
        name='politician_statistic'
    ),
    url(r'^politician/(?P<politician_id>\d+)/statistic/spider/$',
        views.politician_statistic_spider_view,
        name='politician_statistic_spider'
    ),

    # party urls

    url(r'^party/(?P<party_name>\w+)/login/$',
        views.party_login_view,
        name='party_login'
    ),
    url(r'^party/(?P<party_name>\w+)/logout/$',
        views.party_logout_view,
        name='party_logout'
    ),
    url(r'^party/(?P<party_name>\w+)/$',
        views.party_dashboard_view,
        name='party_dashboard'
    ),
    url(r'^party/(?P<party_name>\w+)/export/$',
        views.party_export_view,
        name='party_export'
    ),
    url(r'^party/(?P<party_name>\w+)/politician/add/$',
        views.party_politician_add_view,
        name='party_politician_add'
    ),
    url(r'^party/(?P<party_name>\w+)/politician/(?P<politician_id>\d+)/edit/$',
        views.party_politician_edit_view,
        name='party_politician_edit'
    ),
    url(
        r'^party/(?P<party_name>\w+)/politician/(?P<politician_id>\d+)/delete/$',
        views.party_politician_delete_view,
        name='party_politician_delete'
    ),
)
