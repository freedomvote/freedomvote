from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from core import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^parlamentarier/(?P<unique_url>.+)/$', views.politician_view),
    url(r'^answer/$', views.answer_view),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
