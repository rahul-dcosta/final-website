from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def blog(request):
    return render(request, 'base/blog.html')

def contact(request):
    return render(request, 'base/contact.html')

def experience(request):
    return render(request, 'base/experience.html')

def other(request):
    return render(request, 'base/other.html')

def projskills(request):
    return render(request, 'base/projskills.html')
