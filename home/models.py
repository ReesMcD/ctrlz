from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks


class HomePage(Page):
    """Home page model."""

    content = StreamField(
        [
            ("featured", blocks.FeaturedBlock()),
            ("title", blocks.TitleBlock()),
            ("text", blocks.TextBlock()),
            ("richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    def get_context(self, request):
        context = super().get_context(request)
        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
