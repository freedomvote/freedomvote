from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from core import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',                                   views.citizen_view,             name='citizen'),
    url(r'^parlamentarier/(?P<unique_url>.+)/$', views.politician_view,          name='politician'),
    url(r'^detail/(?P<politician_id>\d+)/$',     views.detail_view,              name='detail'),
    url(r'^statistic/(?P<politician_id>\d+)/$',  views.statistic_view,           name='statistic'),
    url(r'^answer/$',                            views.answer_view,              name='answer'),
    url(r'^share/$',                             views.calculate_statistic_view, name='share'),
    url(r'^retract/$',                           views.retract_statistic_view,   name='retract'),
    url(r'^admin/',                              include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
