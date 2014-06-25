# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fancypages', '0004_fourcolumnlayoutblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorizontalSeparatorBlock',
            fields=[
                ('contentblock_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to='fancypages.ContentBlock')),
            ],
            options={
            },
            bases=('fancypages.contentblock',),
        ),
    ]
