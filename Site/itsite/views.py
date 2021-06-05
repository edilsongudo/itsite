from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from itsite.forms import *
from itsite.models import *
from django.contrib.auth.decorators import login_required


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
            send_email(subject=subject, message=message,
                       file=file, from_whom=from_whom, to_whom=to_whom)
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
            send_email(subject=subject, message=message,
                       file=file, from_whom=from_whom, to_whom=to_whom)
            form.save()
            return redirect('thankyou')
        else:
            messages.warning(request, form.errors.as_text())

    return render(request, 'itsite/hire.html', {'form': form})


def calculator(request):
    if request.user.is_staff:
        return render(request, 'itsite/calculator.html')
    else:
        return HttpResponse('<h1>Unauthorized<h1>', status=401)
