# Generated by Django 3.0.3 on 2020-04-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20200418_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interest',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='interest_amt',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='total_amt',
            field=models.FloatField(max_length=12, null=True),
        ),
    ]
