from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from itsite.forms import *
from itsite.models import *
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from django.conf import settings
import os
import phonenumbers
from .utils import get_geo


def send_message(body):
    try:
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=body, from_=settings.TWILIO_PHONE_NUMBER, to=settings.PHONE_NUMBER)
    except Exception as e:
        print(e)


def send_email(subject, message, file, from_whom, to_whom):
    try:
        email = EmailMessage(subject, message, from_whom,
                             to_whom, headers={'Reply-To': to_whom})
        if file:
            email.attach(file.name, file.read(), file.content_type)
        email.send()
    except Exception as e:
        print(e)


def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location(request):
    try:
        ip = get_ip(request)
        country, city, lat, lon = get_geo(ip)
        return country
    except Exception as e:
        print(e)
        return ''


def set_cookies_in_response(request, response):
    referer = request.META.get('HTTP_REFERER')
    if referer is not None:
        if not 'referer' in request.COOKIES:
            response.set_cookie("referer", referer)
    return response


def home(request):
    print(get_location(request))
    response = render(request, 'itsite/home.html')
    set_cookies_in_response(request, response)
    return set_cookies_in_response(request, response)


def thankyou(request):
    return render(request, 'itsite/thankyou.html')


def job(request, slug):
    job = Post.objects.get(slug=slug)
    response = render(request, 'itsite/job.html', {'job': job})
    return set_cookies_in_response(request, response)


def jobs(request):
    jobs = Post.objects.all()
    response = render(request, 'itsite/jobs.html', {'jobs': jobs})
    return set_cookies_in_response(request, response)

def apply(request):

    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            z = phonenumbers.parse(form.cleaned_data['full_number'], None)
            if not phonenumbers.is_valid_number(z):
                messages.warning(request, 'Please type a valid phone number')
                return render(request, 'itsite/apply.html', {'form': form})
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
            send_message(f"New form submission at shine it.")
            referer = request.COOKIES.get('referer')
            if referer is not None:
                form.instance.referer = referer
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
            z = phonenumbers.parse(form.cleaned_data['full_number'], None)
            if not phonenumbers.is_valid_number(z):
                messages.warning(request, 'Please type a valid phone number')
                return render(request, 'itsite/hire.html', {'form': form})
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
            send_message(f"New form submission at shine it.")
            referer = request.COOKIES.get('referer')
            if referer is not None:
                form.instance.referer = referer
            form.save()
            return redirect('thankyou')
        else:
            messages.warning(request, form.errors.as_text())

    return render(request, 'itsite/hire.html', {'form': form})


def calculator(request):
    if request.user.is_staff:
        return render(request, 'itsite/calculator.html')
    else:
        return HttpResponseForbidden()


def error_404_view(request, exception):
    return render(request, 'itsite/404.html')
