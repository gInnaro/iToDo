from django import template
from main.models import Category, Note

register = template.Library()

@register.simple_tag(name='cat')
def category_tags(username):
    return Category.objects.filter(authors=username)


@register.simple_tag(name='note')
def note_tags(username):
    cats = Category.objects.filter(authors=username).first()
    categorys = Note.objects.filter(authors=username)
    return categorys


