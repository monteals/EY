# Generated by Django 3.1 on 2020-08-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0005_auto_20200821_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emails',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]