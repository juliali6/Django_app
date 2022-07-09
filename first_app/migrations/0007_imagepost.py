# Generated by Django 4.0.4 on 2022-07-03 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/%Y', verbose_name='Photo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_post', to='first_app.post')),
            ],
            options={
                'verbose_name': 'Photo post',
                'verbose_name_plural': 'Photo posts',
            },
        ),
    ]