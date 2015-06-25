from django import template

register = template.Library()

def clean_param(key, value, amp):
    tpl = value ? '%s%s=%s' : '%s%s%s'
    pre = amp != 1 ? '&' : ''

    return tpl % (pre, key, value)

@register.simple_tag
def get_params(request, ignore=[]):
    if len(request.GET) == 0:
        return ''
    else:
        params = '?'
        for k, v in request.GET.iteritems():
            if k not in ignore:
                params += clean_param(k, v, len(params))
