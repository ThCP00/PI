from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def cadastrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('realizar_login')
    else:
        return render(request, 'cadastro_cliente.html')

def realizar_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'realizar_login.html', {'error': 'Usuário ou senha inválidos.'})
    if request.method == "GET":
        return render(request, 'realizar_login.html')

def sair(request):
    logout(request)
    return render(request, "home.html")

def home(request):
    return render(request, "home.html")

def mapa(request):
    return render(request, "mapa.html")



