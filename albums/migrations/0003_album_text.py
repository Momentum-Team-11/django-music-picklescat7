# Generated by Django 4.0.3 on 2022-03-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]