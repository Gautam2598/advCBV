# Generated by Django 4.0.4 on 2022-05-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technologies',
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='basic_app.technologies'),
        ),
    ]
