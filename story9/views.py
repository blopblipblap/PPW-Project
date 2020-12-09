from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = UserCreationForm(request.POST or None)
    if (form.is_valid and request.method == 'POST'):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Akun telah dibuat untuk {username}')
        return redirect('login')

    response = {'form' : UserCreationForm()}
    return render(request, 'story9/story9.html', response)

    