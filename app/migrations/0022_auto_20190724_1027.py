# Generated by Django 2.2.3 on 2019-07-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190724_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reply',
            name='viewer',
            field=models.CharField(max_length=10),
        ),
    ]
