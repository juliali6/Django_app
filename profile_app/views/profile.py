
from django.shortcuts import render, redirect

from django.views import View

from profile_app.models import Profile


class ProfileUserView(View):
    def get(self, request):
        context = {
            'title': 'Profile',
        }
        return render(request, "profile.html", context)
        # return redirect("auth_page")









