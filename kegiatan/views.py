from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Input_Form_Kegiatan, Input_Form_Orang
from .models import Kegiatan, Orang

# Create your views here.
def kegiatann(request):
    kegiatan = Kegiatan.objects.all()
    orang = Orang.objects.all()
    response = {'kegiatan' : Input_Form_Kegiatan,
                'kegiatans' : kegiatan,
                'orangs' : orang}
    if (request.method == 'POST'):
        kegiatan = Kegiatan.objects.get(id = request.POST.get('nama'))
        peserta = Orang.objects.create(orang = request.POST['orang'], kegiatan = kegiatan)
        return HttpResponseRedirect('/kegiatan/')
    return render(request, 'kegiatan/kegiatan.html', response)

def savekegiatan(request):
    form = Input_Form_Kegiatan(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/kegiatan/')
    else:
        return HttpResponseRedirect('/kegiatan/')

def saveorang(request, angka):
    obj = Kegiatan.objects.get(id=angka)
    form = Input_Form_Orang(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        orang = Orang.objects.create(orang=request.POST['orang'], kegiatan=obj)
        return HttpResponseRedirect('/kegiatan/')
    else :
        return HttpResponseRedirect('/kegiatan/')

def details(request, angka):
    obj = Kegiatan.objects.get(id=angka)
    response = {'detail' : obj,
                'urang' : Input_Form_Orang,}
    return render(request, 'kegiatan/display.html', response)
    






   

