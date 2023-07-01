from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def info(request):
    return render(request, 'info.html')

def blog(request):
    posts = Post.objects.all()
    context = {
        'Posts':posts,
    }
    return render(request, 'blog.html', context=context)

def post(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html',{'post':post})