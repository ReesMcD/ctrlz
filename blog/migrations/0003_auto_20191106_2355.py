# Generated by Django 2.2.7 on 2019-11-06 23:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='ArticlePage',
        ),
    ]
