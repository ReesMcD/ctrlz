from wagtail.core import blocks


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

# TODO: Add Featured Article Block
# TODO: Add Recent Article Block
# TODO: Maybe Navbar Block
