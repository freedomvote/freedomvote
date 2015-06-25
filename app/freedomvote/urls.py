from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('')

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^debug/', include(debug_toolbar.urls)),
    )

urlpatterns += patterns('',
    url(r'^admin/' , include(admin.site.urls)) ,
    url(r'^'       , include('core.urls'))     ,
    url(r'^'       , include('cms.urls'))      ,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
