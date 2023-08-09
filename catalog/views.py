from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Post,TypeUser, User, Url
import json
from django.db.models import Sum,Value
from django.db.models.functions import Coalesce
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def info(request):
    return render(request, 'info.html')

def send(request,total_score):
    types = TypeUser.objects.all()
    return render(request,'sentFootprint.html',{'total_score':total_score,'types':types,'mesagge':''})

def games(request):
    urls=Url.objects.all()
    return render(request,'games.html',{'urls':urls})

def play(request,id):
    game = Url.objects.get(id=id)
    return render(request,'play.html',{'game':game})
    

def blog(request):
    posts = Post.objects.all()
    context = {
        'Posts':posts,
    }
    return render(request, 'blog.html', context=context)

def post(request,id):
    post = Post.objects.get(id=id)
    images = post.images.all()
    return render(request, 'post.html',{'post':post,'images':images})

def test(request):
    return render(request, 'test.html')

def saved(request,score,name,type):
    types = TypeUser.objects.all()
    if(User.objects.filter(name=name).exists()):
        return render(request, 'sentFootprint.html',{'mesagge':'Ya se registro una huella con ese nombre','types':types,'total_score':score})
    else:
        user = User(name=name,age=0,CarbonFootprint=score,Type=TypeUser.objects.get(name=type))
        user.save()
        return render(request, 'SuccesfullSave.html')
    
def statistics(request):
    total = User.objects.all().aggregate(Sum('CarbonFootprint'))
    Estudiantes = User.objects.filter(Type=TypeUser.objects.get(name="Estudiante")).aggregate(Sum('CarbonFootprint'))
    Profesores = User.objects.filter(Type=TypeUser.objects.get(name="Profesor")).aggregate(Sum('CarbonFootprint'))
    Administrativos = User.objects.filter(Type=TypeUser.objects.get(name="Administrativo")).aggregate(Sum('CarbonFootprint'))
    Padres = User.objects.filter(Type=TypeUser.objects.get(name="Padre de familia")).aggregate(Sum('CarbonFootprint'))

    # Manually check and set context variables to 0 if they are None
    context = {
        'Estudiantes': Estudiantes['CarbonFootprint__sum'] if Estudiantes['CarbonFootprint__sum'] is not None else 0,
        'Profesores': Profesores['CarbonFootprint__sum'] if Profesores['CarbonFootprint__sum'] is not None else 0,
        'Administrativos': Administrativos['CarbonFootprint__sum'] if Administrativos['CarbonFootprint__sum'] is not None else 0,
        'Padres': Padres['CarbonFootprint__sum'] if Padres['CarbonFootprint__sum'] is not None else 0,
        'total': total['CarbonFootprint__sum'] if total['CarbonFootprint__sum'] is not None else 0,
    }
    return render(request, 'HuellaColsam.html', context=context)