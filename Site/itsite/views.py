from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings
from itsite.forms import ApplyForm


def home(request):
    return render(request, 'itsite/home.html')


def thankyou(request):
    return render(request, 'itsite/thankyou.html')


def send_email(subject, message, file=False, from_whom, to_whom):
    email = EmailMessage(subject, message, from_whom,
                         to_whom, headers={'Reply-To': to_whom})
    if file:
        email.attach(file.name, file.read(), file.content_type)
    email.send()


def apply(request):

    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            subject = "New form submission"
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
