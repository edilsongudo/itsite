from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from itsite.forms import ApplyForm

# Create your views here.


def home(request):
    return render(request, 'itsite/home.html')


def thankyou(request):
    return render(request, 'itsite/thankyou.html')


def apply(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            message = f"Email: {form.cleaned_data['email']}\nName: {form.cleaned_data['name']}"
            email = EmailMessage('New Cv submission', message, settings.EMAIL_HOST_USER, [
                settings.EMAIL_HOST_USER], headers={'Reply-To': settings.EMAIL_HOST_USER})
            if request.FILES:
                file = request.FILES['cv']
                email.attach(file.name, file.read(), file.content_type)
            email.send()
            form.save()
            return redirect('thankyou')
        else:
            form = ApplyForm(request.POST)
            print('invalid form')
    else:
        print('get request')
    return render(request, 'itsite/apply.html', {'form': ApplyForm})
