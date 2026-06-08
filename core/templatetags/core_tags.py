from django import template

register = template.Library()


@register.filter
def split_paragraphs(value):
    """Split text into paragraphs on double newlines."""
    if not value:
        return []
    paras = [p.strip() for p in value.split('\n\n') if p.strip()]
    return paras if paras else [value]
