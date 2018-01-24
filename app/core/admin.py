from django.conf import settings
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
import models


class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort']


class PartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'shortname']


class PoliticianAdmin(admin.ModelAdmin):
    def unique_url(self, obj):
        return '%s%s' % (
            settings.BASE_URL,
            reverse('politician_edit_profile', args=(obj.unique_key,))
        )
    unique_url.short_description = _('unique_url')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return ()

    list_display = ['first_name', 'last_name', 'email', 'unique_url']
    readonly_fields = ('unique_url',)
    exclude = ('unique_key',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class QuestionAdmin(admin.ModelAdmin):
    def get_category(self, obj):
        return obj.category.__unicode__()
    get_category.short_description = _('category')

    list_display = ['question_number', 'get_category', 'text']


class RegistrationKeyInline(admin.StackedInline):
    model = models.RegistrationKey
    can_delete = False
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (RegistrationKeyInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(models.State,      StateAdmin)
admin.site.register(models.Party,      PartyAdmin)
admin.site.register(models.Politician, PoliticianAdmin)
admin.site.register(models.Category,   CategoryAdmin)
admin.site.register(models.Question,   QuestionAdmin)
