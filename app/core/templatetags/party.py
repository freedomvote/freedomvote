from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def party_tag(party):
    return u'<span title="{}" class="party-tag" style="color:{};background-color:{}"><span>{}</span></span>'.format(
        party.name,
        party.font_color,
        party.background_color,
        party.shortname
    )
