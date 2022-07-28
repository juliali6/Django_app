import os

from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import View

from profile_app.forms.registration import RegistrationForm
from profile_app.tasks import email_reg_task


class RegistrationView(View):
    """View for registration."""

    @staticmethod
    def get(request):

        if request.user.is_authenticated:
            return redirect('posts')

        form = RegistrationForm()
        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

    @staticmethod
    def post(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            email_reg_task()
            email_reg_task()
            send_mail('Hello, my friend!',
                      'You are awesome!',
                      str(os.getenv('EMAIL_HOST_USER')),
                      [user.email])
            login(request, user)
            return redirect('/')

        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

