# Generated by Django 2.2.3 on 2019-07-22 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_post_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='app.Post'),
        ),
    ]
