# Generated by Django 3.0.3 on 2020-04-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20200419_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interest',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='interest_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='total_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
