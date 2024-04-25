from django.db import models
from django import forms

# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nome', 'idade', 'email', 'telefone']