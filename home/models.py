from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks


class HomePage(Page):
    """Home page model."""

    # TODO: Clean up homepage names
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner = StreamField(
        [
            ("featured", blocks.FeaturedBlock()),
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
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        PageChooserPanel("banner_cta"),
        StreamFieldPanel("banner"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
