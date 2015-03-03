from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from core import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search/$',                              views.search_view,            name='search'),
    url(r'^compare/$',                             views.compare_view,           name='compare'),
    url(r'^politician/(?P<unique_url>.+)/$',       views.politician_view,        name='politician'),
    url(r'^profile/(?P<politician_id>\d+)/$',      views.profile_view,           name='profile'),
    url(r'^profile_info/(?P<politician_id>\d+)/$', views.profile_info_view,      name='profile_info'),
    url(r'^politician_answer/$',                   views.politician_answer_view, name='politician_answer'),
    url(r'^publish/$',                             views.publish_view,           name='publish'),
    url(r'^unpublish/$',                           views.unpublish_view,         name='unpublish'),
    url(r'^admin/',                                include(admin.site.urls)),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
