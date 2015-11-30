# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('supplies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('keywords_string', models.CharField(editable=False, blank=True, max_length=500)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(verbose_name='URL', help_text='Leave blank to have the URL auto-generated from the title.', blank=True, max_length=2000, null=True)),
                ('_meta_title', models.CharField(verbose_name='Title', help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', blank=True, max_length=500, null=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True)),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(verbose_name='Status', help_text='With Draft chosen, will only be shown for admin users on the site.', choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('publish_date', models.DateTimeField(verbose_name='Published from', help_text="With Published chosen, won't be shown until this time", blank=True, db_index=True, null=True)),
                ('expiry_date', models.DateTimeField(verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time", blank=True, null=True)),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='supplies.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
    ]
