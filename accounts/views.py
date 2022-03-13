from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import FormContato


# REALIZAR LOGIN
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso!')
        return redirect('acesso')


# ACESSADO
@login_required(redirect_field_name='login')
def acesso(request):
    return render(request, 'accounts/acesso.html')

# ACESSO AO DASHBOARD


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Confira os dados para salvar o cadastro.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    form.save()
    messages.success(request, f'Cadastro de {request.POST.get("nome")} realizado com sucesso.')
    return redirect('dashboard')


# REALIZAR LOGout
def logout(request):
    auth.logout(request)
    return redirect('index')
