from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog

admin.autodiscover()

urlpatterns = [
    url(r"^jsi18n/$", JavaScriptCatalog.as_view(), {}, name="javascript-catalog"),
    url(r"^admin/", admin.site.urls),
    url(r"^api/", include("api.urls")),
    url(r"^", include("core.urls")),
    url(r"^", include("cms.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
