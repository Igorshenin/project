from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    words = ['придурок', 'сволочь', 'гад', 'fuck']
    for word in words:
        if word in value:
            value = value.replace(word, '[цензура]')
    return str(value)

