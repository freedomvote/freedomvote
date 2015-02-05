from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import models

class StateAdmin(admin.ModelAdmin):
    list_display = ['name']


class PartyAdmin(admin.ModelAdmin):
    list_display = ['name']


class PoliticianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    readonly_fields = ('unique_url',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class QuestionAdmin(admin.ModelAdmin):
    def get_category(self, obj):
        return obj.category.__str__()
    get_category.short_description = _('category')

    list_display = ['question_number', 'get_category', 'text']

admin.site.register(models.State,      StateAdmin)
admin.site.register(models.Party,      PartyAdmin)
admin.site.register(models.Politician, PoliticianAdmin)
admin.site.register(models.Category,   CategoryAdmin)
admin.site.register(models.Question,   QuestionAdmin)
