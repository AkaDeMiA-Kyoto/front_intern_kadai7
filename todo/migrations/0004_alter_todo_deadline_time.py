# Generated by Django 4.0.5 on 2022-06-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_contents_alter_todo_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_time',
            field=models.TimeField(blank=True, verbose_name='期日(時間)'),
        ),
    ]
