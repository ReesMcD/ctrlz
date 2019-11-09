# Generated by Django 2.2.7 on 2019-11-09 18:42

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0006_articlepagegalleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.ArticlePage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_articlepagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='articlepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.ArticlePageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
