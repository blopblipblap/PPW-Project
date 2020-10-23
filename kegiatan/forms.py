from django import forms
from .models import Kegiatan, Orang

class Input_Form_Kegiatan(forms.ModelForm) :
    class Meta:
        model = Kegiatan
        fields = ['nama']

    error_messages = {
        'required' : 'Please Type'
    }

    input_attrs_kegiatan = {
        'type' : 'text',
        'placeholder' : 'Tambah Kegiatan',
        'class' : 'inputbox',
    }

    nama = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_kegiatan))

class Input_Form_Orang(forms.ModelForm):
    class Meta:
        model = Orang
        fields = ['orang']

    error_messages = {
        'required' : 'Please Type'
    }

    input_attrs_orang = {
        'type' : 'text',
        'placeholder' : 'Nama kamu',
        'class' : 'inputbox',
        'name' : 'id',
    }

    orang = forms.CharField(label='', required=True, max_length=150, widget=forms.TextInput(attrs=input_attrs_orang))