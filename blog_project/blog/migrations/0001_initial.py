# Generated by Django 2.1.4 on 2018-12-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('subheader', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
