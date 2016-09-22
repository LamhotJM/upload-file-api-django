# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import commentengine.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterComment',
            fields=[
                ('commentid', models.IntegerField(serialize=False, primary_key=True)),
                ('userid', models.CharField(max_length=100, null=True, blank=True)),
                ('loanid', models.CharField(max_length=100, null=True, blank=True)),
                ('comment', models.CharField(max_length=225, null=True, blank=True)),
                ('file_upload', models.FileField(max_length=254, null=True, upload_to=commentengine.models.get_image_path)),
                ('context_id', models.IntegerField(blank=True)),
                ('context_scope', models.CharField(max_length=400, null=True, blank=True)),
                ('status', models.IntegerField(blank=True)),
                ('createdby', models.CharField(max_length=25, null=True, blank=True)),
                ('createdfrom', models.CharField(max_length=60, null=True, blank=True)),
                ('createddate', models.DateTimeField(editable=False)),
                ('modifiedby', models.CharField(max_length=25, null=True, blank=True)),
                ('modifiedfrom', models.CharField(max_length=60, null=True)),
                ('modifieddate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': True,
            },
        ),
    ]
