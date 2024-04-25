from django.shortcuts import render
from .models import FormularioForm,Formulario

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            print(nome,idade,email,telefone,sep = "\n")
            form.save()
            formularios = Formulario.objects.all()
            return render(request,'cadastros.html',{'formularios' : formularios})

    else:
        form = FormularioForm()
        return render(request, 'index.html', {'form': form})
    
    

    


