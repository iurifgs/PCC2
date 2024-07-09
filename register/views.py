from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, AdminLoginForm
from django.contrib.auth.decorators import login_required, user_passes_test
from pet.models import Animal


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required
def index(request):
    return render(request, 'pet/index.html')

@login_required
def user_index(request):
    animais = Animal.objects.all()
    return render(request, 'pet/user_index.html', {'animais': animais})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_index')
        else:
            return render(request, 'registration/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'registration/login.html')

def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    return render(request, 'registration/admin_login.html', {'form': form, 'error': 'Conta não cadastrada como administrador'})
            else:
                return render(request, 'registration/admin_login.html', {'form': form, 'error': 'Credenciais inválidas'})
        else:
            return render(request, 'registration/admin_login.html', {'form': form, 'error': 'Formulário inválido'})
    else:
        form = AdminLoginForm()
    return render(request, 'registration/admin_login.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    animais = Animal.objects.all()
    return render(request, 'pet/index.html', {'animais': animais})