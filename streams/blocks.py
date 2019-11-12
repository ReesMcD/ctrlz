from wagtail.core import blocks


class TitleAndTextStreamBlock(blocks.StructBlock):
    """Title and Text Stream Block"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichTextSteamBlock(blocks.RichTextBlock):
    """Rich Text Stream Block"""

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "doc-full"
        label = "RichText"
