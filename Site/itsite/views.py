from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'itsite/home.html')


def hire(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form', message, settings.EMAIL_HOST_USER, [
                  'edilson4football@gmail.com'], fail_silently=False)
    return render(request, 'itsite/hire.html')
