# Generated by Django 4.0.5 on 2022-06-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.FileField(upload_to='media/')),
            ],
            options={
                'db_table': 'Audio_store',
            },
        ),
    ]