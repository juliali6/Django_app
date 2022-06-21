from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import View

from profile_app.forms.registration import RegistrationForm


class RegistrationView(View):
    @staticmethod
    def get(request):
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
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'from@example.com',
            #     ['to@example.com'],
            #     fail_silently=False,
            # )
            return redirect('/')

        context = {
            'reg_form': form,
        }
        return render(request, 'registration_page.html', context)

