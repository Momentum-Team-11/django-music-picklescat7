# Generated by Django 4.0.3 on 2022-03-06 00:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
