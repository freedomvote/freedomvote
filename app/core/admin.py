from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import models
from django.core.urlresolvers import reverse
from django.conf import settings

class StateAdmin(admin.ModelAdmin):
    list_display = ['name']


class PartyAdmin(admin.ModelAdmin):
    list_display = ['name']


class PoliticianAdmin(admin.ModelAdmin):
    def full_unique_url(self, obj):
        return '%s%s' % (
            settings.BASE_URL,
            reverse('politician', args=(obj.unique_url,))
        )
    full_unique_url.short_description = _('full_unique_url')

    list_display = ['first_name', 'last_name', 'email', 'full_unique_url']
    readonly_fields = ('full_unique_url',)
    exclude = ('unique_url',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class LinkTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class QuestionAdmin(admin.ModelAdmin):
    def get_category(self, obj):
        return obj.category.__unicode__()
    get_category.short_description = _('category')

    list_display = ['question_number', 'get_category', 'text']

admin.site.register(models.State,      StateAdmin)
admin.site.register(models.Party,      PartyAdmin)
admin.site.register(models.Politician, PoliticianAdmin)
admin.site.register(models.Category,   CategoryAdmin)
admin.site.register(models.Question,   QuestionAdmin)
admin.site.register(models.LinkType,   LinkTypeAdmin)
