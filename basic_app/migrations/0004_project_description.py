# Generated by Django 4.0.4 on 2022-05-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_remove_project_employees_project_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='Hello', max_length=1000),
        ),
    ]
