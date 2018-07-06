from django import template

register = template.Library()

def clean_param(key, value, amp):
    tpl = '{}{}={}'.format(pre, key, vlaue) if value else '{}{}{}'.format(pre, key, value)
    pre = '&' if amp != 1 else ''

    return tpl

@register.simple_tag
def get_params(request, ignore=[]):
    if len(request.GET) == 0:
        return ''
    else:
        params = '?'
        for k, v in request.GET.iteritems():
            if k not in ignore:
                params += clean_param(k, v, len(params))
