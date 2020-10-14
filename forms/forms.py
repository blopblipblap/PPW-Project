from django import forms
from .models import Matkul

class Input_Form(forms.ModelForm) :
    class Meta:
        model = Matkul
        fields = ['name', 'dosen', 'sks', 'deskripsi', 'semester', 'kelas']

    error_messages = {
        'required' : 'Please Type'
    }

    input_attrs_nama = {
        'type' : 'text',
        'placeholder' : 'Nama Matkul',
        'class' : 'inputbox',
    }

    input_attrs_dosen = {
        'type' : 'text',
        'placeholder' : 'Nama Dosen',
        'class' : 'inputbox',
    }

    input_attrs_sks = {
        'type' : 'text',
        'placeholder' : 'Bobot SKS',
        'class' : 'inputbox',
    }

    input_attrs_deskripsi = {
        'type' : 'text',
        'placeholder' : 'Deskripsi',
        'class' : 'inputbox',
    }

    input_attrs_semester = {
        'type' : 'text',
        'placeholder' : 'Semester',
        'class' : 'inputbox',
    }

    input_attrs_kelas = {
        'type' : 'text',
        'placeholder' : 'Ruang Kelas',
        'class' : 'inputbox',
    }

    name = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_nama))
    dosen = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_dosen))
    sks = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_sks))
    deskripsi = forms.CharField(label='', required=True, max_length=150, widget=forms.Textarea(attrs=input_attrs_deskripsi))
    semester = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_semester))
    kelas = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_kelas))
    