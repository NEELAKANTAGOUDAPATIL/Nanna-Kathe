# Generated by Django 3.0.3 on 2020-04-16 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
