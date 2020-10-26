from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
        FieldPanel,
        FieldRowPanel,
        InlinePanel,
        MultiFieldPanel,
        PageChooserPanel,
        StreamFieldPanel,
)

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page, Orderable
from wagtail.core import blocks
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock

class ExperienceBlock(blocks.StructBlock):
    location = blocks.CharBlock(required=True, max_length=63)
    location_site = blocks.URLBlock(required=True, max_length=255)
    time_period = blocks.CharBlock(required=False)
    description = blocks.RichTextBlock(required=True)

    class Meta:
        icon="doc-full"
        template="blocks/experience_block.html"

class HomePage(Page):
    name_display = models.CharField(
            max_length=127,
            default='Your name here'
            )

    banner_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            help_text='Wide Welcome Banner Image'
    )
    intro_text = models.CharField(
            max_length=255,
            default='Intro Text',
            help_text='Text to display in the middle of the banner'
    )
    profile_pic = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            help_text='Profile Picture'
    )

    bio = RichTextField(blank=True)
    edu_history = StreamField([
        ('item', ExperienceBlock()),
    ], null=True)

    motivation_header = models.CharField(
            max_length=255,
            default='Motivation',
            help_text='Title for motivation section'
    )
    motivation = RichTextField(blank=True)

    work_history = StreamField([
        ('item', ExperienceBlock()),
    ], null=True)

    content_panels = Page.content_panels + [
            MultiFieldPanel([
                FieldPanel('name_display', classname="full"),
                ImageChooserPanel('banner_image'),
                FieldPanel('intro_text', classname="full"),
                ], heading='Big Intro Section'),
            MultiFieldPanel([
                ImageChooserPanel('profile_pic'),
                FieldPanel('bio'),
                ], heading='Biography Section'),
            MultiFieldPanel([
                FieldPanel('motivation_header'),
                FieldPanel('motivation'),
            ], heading='Motivation Section'),
            StreamFieldPanel('edu_history', heading='Education History'),
            StreamFieldPanel('work_history', heading='Work History')
            ]
