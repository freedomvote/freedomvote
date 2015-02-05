from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from core import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^parlamentarier/(?P<unique_url>\w+)/$', views.politician_view),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
