from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('blog', views.blog, name='blog'),
    path('post/<int:id>', views.post, name='post'),
    path('test', views.test, name='test'),
    path('games',views.games,name='games'),
    path('play/<int:id>',views.play,name='play'),
    path('sendFoot/<int:total_score>',views.send,name="send"),
    path('saved/<int:score>/<str:name>/<str:type>',views.saved,name="saved"),
    path('statistics',views.statistics,name="statistics"),
]
