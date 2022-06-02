from django.shortcuts import render, redirect
from django.views import View

from first_app.models import Profile


class Profile_User(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            contex = {
                'title': 'Profile',
                'avatar': user,
            }
            return render(request, "profile.html", contex)
        return redirect("auth_page")
