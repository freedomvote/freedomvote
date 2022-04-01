from django import template

register = template.Library()


@register.filter()
def label_with_class(value, arg):
    return value.label_tag(attrs={"class": arg})
