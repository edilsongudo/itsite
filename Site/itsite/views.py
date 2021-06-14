from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from itsite.forms import *
from itsite.models import *
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from django.conf import settings
import os


def send_message(body):
    try:
        print('Sending Message...')
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body, from_=settings.TWILIO_PHONE_NUMBER, to=settings.PHONE_NUMBER)
    except Exception as e:
        print(e)


def send_email(subject, message, file, from_whom, to_whom):
    email = EmailMessage(subject, message, from_whom,
                         to_whom, headers={'Reply-To': to_whom})
    if file:
        email.attach(file.name, file.read(), file.content_type)
    email.send()


def home(request):
    return render(request, 'itsite/home.html')


def thankyou(request):
    return render(request, 'itsite/thankyou.html')


def job(request, slug):
    job = Post.objects.get(slug=slug)
    return render(request, 'itsite/job.html', {'job': job})

def jobs(request):
    jobs = Post.objects.all()
    return render(request, 'itsite/jobs.html', {'jobs': jobs})


def apply(request):

    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            subject = "New cv submission"
            message = f"Email: {form.cleaned_data['email']}\nName: {form.cleaned_data['name']}"
            from_whom = settings.EMAIL_HOST_USER
            to_whom = [settings.EMAIL_HOST_USER]
            file = request.FILES['cv']
            extension = os.path.splitext(file.name)[1]
            valid_extensions = ['.pdf', '.doc', '.docx']
            if extension not in valid_extensions:
                messages.warning(request, 'Uploaded File type not Supported')
                return render(request, 'itsite/apply.html', {'form': form})
            send_email(subject=subject, message=message,
                       file=file, from_whom=from_whom, to_whom=to_whom)
            send_message(f"New form submission ar shine it.")
            form.save()
            return redirect('thankyou')
        else:
            messages.warning(request, form.errors.as_text())

    return render(request, 'itsite/apply.html', {'form': form})


def hire(request):

    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)

        if form.is_valid():
            subject = "New job request"
            message = f"Email: {form.cleaned_data['email']}\nName: {form.cleaned_data['name']}"
            from_whom = settings.EMAIL_HOST_USER
            to_whom = [settings.EMAIL_HOST_USER]
            file = False
            if request.FILES:
                file = request.FILES['document']
                extension = os.path.splitext(file.name)[1]
                valid_extensions = ['.pdf', '.doc', '.docx']
                if extension not in valid_extensions:
                    messages.warning(
                        request, 'Uploaded File type not Supported')
                    return render(request, 'itsite/hire.html', {'form': form})
            send_email(subject=subject, message=message,
                       file=file, from_whom=from_whom, to_whom=to_whom)
            send_message(f"New form submission ar shine it.")
            form.save()
            return redirect('thankyou')
        else:
            messages.warning(request, form.errors.as_text())

    return render(request, 'itsite/hire.html', {'form': form})


def calculator(request):
    if request.user.is_staff:
        return render(request, 'itsite/calculator.html')
    else:
        return HttpResponse('<h1>Forbidden<h1>', status=403)
