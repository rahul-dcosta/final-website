from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def blog(request):
    return render(request, 'base/blog.html')

def contact(request):
    # if request.method == 'POST':
    #     message = request.POST['message']
    #     send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['rahuldc2000@gmail.com'], fail_silently=False)
    return render(request, 'base/contact.html')

def experience(request):
    return render(request, 'base/experience.html')

def other(request):
    return render(request, 'base/other.html')

def projskills(request):
    return render(request, 'base/projskills.html')
