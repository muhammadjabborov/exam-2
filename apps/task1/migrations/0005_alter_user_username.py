# Generated by Django 4.2.1 on 2023-05-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_alter_user_phone_number_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
