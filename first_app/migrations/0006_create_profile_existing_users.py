from django.db import migrations


def create_profile_for_existing_user(apps, schenas_editors):
    user_model = apps.get.model('auth', 'User')
    profile_model = apps.get.model('first_app', 'Profile')

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):
    dependencies = (
        ('first_app', '0005_alter_post_image')
    )

    operations = (
        migrations.RunPython(create_profile_for_existing_user),
    )
