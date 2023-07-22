from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Post,TypeUser, User
import json
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
    return render(request,'games.html')

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
        return render(request, 'sentFootprint.html',{'mesagge':'Ya se registro una huella con ese nombre','types':types})
    else:
        user = User(name=name,age=0,CarbonFootprint=score,Type=TypeUser.objects.get(name=type))
        user.save()
        return render(request, 'Succesfullsave.html')