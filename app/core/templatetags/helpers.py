from django import template
from django.conf import settings

register = template.Library()

def clean_param(key, value, amp):
    if value == '0' or value == '':
        return ''

    tpl = '%s%s=%s' if value else '%s%s%s'
    pre = '&' if amp != 1 else ''

    return tpl % (pre, key, value)

@register.simple_tag
def get_params(request, *args, **kwargs):
    params = '?'
    for k, v in request.GET.items():
        if k not in args:
            params += clean_param(k, v, len(params))

    if kwargs.get('add'):
        params += '&' + kwargs['add'] if not len(params) == 1 else kwargs['add']

    if params == '?':
        params = ''

    return params

@register.simple_tag
def git_url():
    return settings.GIT_URL
