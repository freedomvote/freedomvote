from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from core import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.citizen_view),
    url(r'^parlamentarier/(?P<unique_url>.+)/$', views.politician_view, name='politician'),
    url(r'^share/(?P<unique_url>.+)/$', views.calculate_statistic_view),
    url(r'^retract/(?P<unique_url>.+)/$', views.retract_statistic_view),
    url(r'^statistic/(?P<politician_id>\d+)/$', views.statistic_view),
    url(r'^detail/(?P<politician_id>\d+)/$', views.detail_view),
    url(r'^answer/$', views.answer_view),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
