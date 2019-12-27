from django import template
from blog.models import ArticlePage

register = template.Library()


@register.inclusion_tag('home/recent_articles.html')
def recent_articles():
    pages = ArticlePage.objects.live().order_by('-date')
    return {'pages': pages}
