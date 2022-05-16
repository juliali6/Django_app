from django.db import migrations


def create_profile_for_existing_users(apps, schema_editors):
    user_model = apps.get_model('auth', 'User')
    profile_model = apps.get_model('first_app', 'Profile')

    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):
    dependencies = (
        ('first_app', '0001_initial'),
    )

    operations = (
        migrations.RunPython(create_profile_for_existing_users),
    )