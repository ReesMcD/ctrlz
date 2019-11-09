from wagtail.snippets.models import register_snippet
from django.db import models
from django import forms

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):

        tag = request.GET.get('tag')
        articlepages = ArticlePage.objects.filter(tags__name=tag)

        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        articlepages = self.get_children().live().order_by('-last_published_at')
        context['articlepages'] = articlepages
        return context


@register_snippet
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Article Categories'


class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ArticlePage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class ArticleTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        articlepages = ArticlePage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['articlepages'] = articlepages
        return context


class ArticlePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)
    categories = ParentalManyToManyField('blog.ArticleCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Article information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class ArticlePageGalleryImage(Orderable):
    page = ParentalKey(ArticlePage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
