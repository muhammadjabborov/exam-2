# Generated by Django 4.2.1 on 2023-05-06 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task2', '0002_alter_company_options_alter_vacancy_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='salary_type',
        ),
    ]
