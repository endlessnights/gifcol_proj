# Generated by Django 3.0.6 on 2020-06-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifcol_app', '0002_auto_20200601_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamodel',
            name='desc',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
