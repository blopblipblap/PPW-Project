from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Input_Form
from .models import Matkul

# Create your views here.
def forms(request):
    response = {'form' : Input_Form}
    return render(request, 'forms/forms.html', response)

def savematkul(request):
    form = Input_Form(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/forms/readmatkul')
    else:
        return HttpResponseRedirect('/forms')

def readmatkul(request):
    response = {'matkuls' : Matkul.objects.all(),
                'form' : Input_Form}
    return render(request, 'forms/forms.html', response)