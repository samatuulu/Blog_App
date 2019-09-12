# Generated by Django 2.2.5 on 2019-09-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=40)),
                ('description', models.TextField()),
                ('date_of_completion', models.DateField(blank=True, default=None)),
            ],
        ),
    ]