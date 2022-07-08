from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from profile_app.models import Profile

from django.views.generic.edit import CreateView


class ProfileUserView(View):
    """View for profile user."""

    def get(self, request):
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            contex = {
                'title': 'Profile',
                'avatar': user,
            }
            return render(request, "profile.html", contex)
        return redirect("auth_page")

#
# class CreateProfilePageView(CreateView):
#     model = Profile
#
#     template_name = 'profile.html'
#     fields = ['last_name', 'first_name', 'email', 'avatar', 'phone']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     success_url = reverse_lazy('profile')

