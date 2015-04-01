from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
    url(r'^candidates/$',                            views.candidates_view,        name='candidates'),
    url(r'^compare/$',                               views.compare_view,           name='compare'),
    url(r'^edit/(?P<unique_key>[^/]+)/$',            views.edit_redirect_view,     name='edit'),
    url(r'^edit/(?P<unique_key>[^/].+)/profile/$',   views.edit_profile_view,      name='edit_profile'),
    url(r'^edit/(?P<unique_key>[^/].+)/questions/$', views.edit_questions_view,    name='edit_questions'),
    url(r'^profile/(?P<politician_id>\d+)/$',        views.profile_view,           name='profile'),
    url(r'^profile_info/(?P<politician_id>\d+)/$',   views.profile_info_view,      name='profile_info'),
    url(r'^politician_answer/$',                     views.politician_answer_view, name='politician_answer'),
    url(r'^publish/$',                               views.publish_view,           name='publish'),
    url(r'^unpublish/$',                             views.unpublish_view,         name='unpublish'),
    url(r'^link/add/$',                              views.add_link_view,          name='add_link'),
    url(r'^link/delete/$',                           views.delete_link_view,       name='delete_link'),
)
