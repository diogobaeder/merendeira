# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, verbose_name='URL', null=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000)),
                ('_meta_title', models.CharField(blank=True, verbose_name='Title', null=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True)),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], help_text='With Draft chosen, will only be shown for admin users on the site.', default=2)),
                ('publish_date', models.DateTimeField(blank=True, verbose_name='Published from', null=True, help_text="With Published chosen, won't be shown until this time", db_index=True)),
                ('expiry_date', models.DateTimeField(blank=True, verbose_name='Expires on', null=True, help_text="With Published chosen, won't be shown after this time")),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
                ('site', models.ForeignKey(to='sites.Site', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
