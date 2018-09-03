from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import javascript_catalog

admin.autodiscover()

urlpatterns = [
    url(r'^jsi18n/$', javascript_catalog, {}, name='javascript-catalog'),
    url(r'^admin/' , include(admin.site.urls)),
    url(r'^api/'   , include('api.urls')),
    url(r'^'       , include('core.urls')),
    url(r'^'       , include('cms.urls')),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
