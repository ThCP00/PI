from django.shortcuts import render

def home(request):
    return render(request, "blog/home.html")

def dashboard(request):
    return render(request, "blog/dashboard.html")

def blog(request):
    return render(request, "blog/blog.html")

# Create your views here.
