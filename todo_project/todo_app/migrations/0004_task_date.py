# Generated by Django 4.2.7 on 2023-12-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-05-14'),
            preserve_default=False,
        ),
    ]
