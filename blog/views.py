from django.shortcuts import render, redirect
from .models import Comentario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import datetime
#import basedosdados as bd


def dashboard(request):
    #df = bd.read_table(dataset_id='br_inmet_bdmep',
    #table_id='estacao',
    #billing_project_id="<210977379576>")
    return render(request, "blog/dashboard.html")

def blog(request):
    return render(request, "blog/blog.html")


def comentario(request):
        if request.method == 'POST':
            comentario = request.POST.get('comentario')
            
            coment = Comentario(
                usuario = request.user,
                comentario=comentario,
            )
            
            coment.save()
        return redirect('blog')

# Create your views here.
