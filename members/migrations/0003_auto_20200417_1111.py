# Generated by Django 3.0.3 on 2020-04-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200416_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
