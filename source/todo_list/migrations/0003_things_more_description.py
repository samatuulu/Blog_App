# Generated by Django 2.2.5 on 2019-09-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20190905_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='things',
            name='more_description',
            field=models.TextField(null=True),
        ),
    ]
