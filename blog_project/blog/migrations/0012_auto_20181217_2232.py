# Generated by Django 2.1.4 on 2018-12-18 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181217_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 18, 6, 32, 38, 408585, tzinfo=utc)),
        ),
    ]
