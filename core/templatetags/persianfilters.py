from django import template

from slugify import slugify

# Create your custom tags and filters here.

register = template.Library()


@register.filter(name='persian_digits')
def persian_digits(value):
    translation_table = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    return value.translate(translation_table)


@register.filter(name='persian_slugify')
def persian_slugify(value):
    return slugify(value, allow_unicode=True)
