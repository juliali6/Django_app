# Generated by Django 4.0.6 on 2022-08-05 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0015_alter_imagepost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagepost',
            options={'verbose_name': 'Photo post', 'verbose_name_plural': 'Photo posts'},
        ),
    ]