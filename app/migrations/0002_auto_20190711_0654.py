# Generated by Django 2.2.3 on 2019-07-11 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Created_on',
            new_name='created_on',
        ),
    ]
