# Generated by Django 3.1.7 on 2021-03-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=3, max_digits=9),
        ),
    ]
