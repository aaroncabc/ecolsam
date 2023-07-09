from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('blog', views.blog, name='blog'),
    path('post/<int:id>', views.post, name='post'),
    path('test', views.test, name='test'),
]
