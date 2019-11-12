from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from streams import blocks


class FlexPage(Page):

    content = StreamField(
        [
            ("title", blocks.TitleBlock()),
            ("text", blocks.TextBlock()),
            ("richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]
