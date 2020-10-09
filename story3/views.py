from django.shortcuts import render

# Create your views here.
def aboutme(request):
    return render(request, 'story3/aboutme.html')

def myexperience(request):
    return render(request, 'story3/myexperience.html')