# Generated by Django 3.1 on 2020-08-21 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('first_last_name', models.CharField(max_length=20)),
                ('second_last_name', models.CharField(max_length=20)),
                ('identification', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('Ot', 'Other'), ('NA', 'N/A')], max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
