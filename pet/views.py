from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from pet.forms import AnimalForm
from .models import Animal
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.urls import reverse
from register.forms import CustomUserCreationForm


@login_required
def create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_dashboard'))
    else:
        form = AnimalForm()
    return render(request, 'pet/formCreate.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_admin:
                return redirect('admin_dashboard')
            else:
                return redirect('user_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

@login_required
def readall(request):
    animais = Animal.objects.all()
    return render(request, "pet/index.html", {'animais': animais})

@login_required
def read(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    return render(request, "pet/detail.html", {'animal': animal})

@login_required
def update(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redirecionar para a página desejada após a atualização
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'pet/formupdate.html', {'form': form, 'animal': animal})

@login_required
def delete(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        animal.delete()
        return HttpResponseRedirect(reverse('admin_dashboard'))
    # Se a requisição não for POST, renderize o template de confirmação de exclusão
    return render(request, 'pet/confirmdelete.html', {'animal': animal})

@login_required
def confirmdelete(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    return render(request, 'pet/confirmdelete.html', {'animal': animal})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    animais = Animal.objects.all()
    return render(request, 'pet/index.html', {'animais': animais})

def user_index(request):
    return render(request, 'pet/user_index.html', {})

def user_detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'pet/user_detail.html', {'animal': animal})

def index(request):
    animals = Animal.objects.all()
    return render(request, '_base.html', {'animals': animals})


def search_animals(request):
    query = request.GET.get('query', '')
    animals = Animal.objects.filter(nome__icontains=query) | Animal.objects.filter(raca__icontains=query)
    results = []
    for animal in animals:
        results.append({
            'nome': animal.nome,
            'raca': animal.raca,
            'data_nascimento': animal.data_nascimento,
            'imagem_url': animal.imagem.url if animal.imagem else '',
            'sexo': animal.get_sexo_display(),
        })
    return JsonResponse(results, safe=False)

def adoption_info(request):
    return render(request, 'pet/adoption_info.html')
