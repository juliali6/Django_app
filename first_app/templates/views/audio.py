from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from first_app.forms.audio import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('successfully_upload')
    else:
        form = UploadFileForm()
    return render(request, 'aud.html', {'form': form})

