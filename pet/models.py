from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Animal(models.Model):
    nome = models.CharField(max_length=50, default='')
    raca = models.CharField(max_length=50, default='Desconhecida', null=True, blank=True)
    data_nascimento = models.DateField(default=str(timezone.now().date()))
    imagem = models.ImageField(upload_to='animais/', blank=True, null=True)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')

    def clean(self):
        # Verifica se a data de nascimento é uma data futura
        if self.data_nascimento > timezone.now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")

    def __str__(self):
        return self.nome


