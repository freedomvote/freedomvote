from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
    url(r'^candidates/$',                          views.candidates_view,        name='candidates'),
    url(r'^compare/$',                             views.compare_view,           name='compare'),
    url(r'^edit/(?P<unique_url>.+)/$',             views.politician_view,        name='politician'),
    url(r'^profile/(?P<politician_id>\d+)/$',      views.profile_view,           name='profile'),
    url(r'^profile_info/(?P<politician_id>\d+)/$', views.profile_info_view,      name='profile_info'),
    url(r'^politician_answer/$',                   views.politician_answer_view, name='politician_answer'),
    url(r'^publish/$',                             views.publish_view,           name='publish'),
    url(r'^unpublish/$',                           views.unpublish_view,         name='unpublish'),
)
