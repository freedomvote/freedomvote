from django import template

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
    for k, v in request.GET.iteritems():
        if k not in args:
            params += clean_param(k, v, len(params))

    if kwargs.get('add'):
        params += '&' + kwargs['add'] if not len(params) == 1 else kwargs['add']

    if params == '?':
        params = ''

    return params
