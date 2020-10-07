from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def aboutme(request):
    return render(request, 'main/aboutme.html')

def myexperience(request):
    return render(request, 'main/myexperience.html')

def story1(request):
    return render(request, 'main/index.html')