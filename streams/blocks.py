from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from blog.models import ArticlePage
from wagtail.core.models import Page


class TitleBlock(blocks.StructBlock):
    """Title Stream Block"""

    title = blocks.CharBlock(required=True, help_text="Add your title")

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"


class TextBlock(blocks.StructBlock):
    """Text Stream Block"""

    text = blocks.CharBlock(required=True, help_text="Add your text")

    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Text"


class RichTextBlock(blocks.RichTextBlock):
    """Rich Text Block"""

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "RichText"


class ThumbnailBlock(blocks.StructBlock):
    page = blocks.PageChooserBlock(required=True, page_type=ArticlePage)
    image = ImageChooserBlock(required=False)

    class Meta:
        label = "Thumbnail"


class FeaturedBlock(blocks.StructBlock):
    thumbnails = blocks.ListBlock(ThumbnailBlock(), max_num=3)

    class Meta:
        template = "streams/featured_block.html"
        icon = "image"
        label = "Featured"
