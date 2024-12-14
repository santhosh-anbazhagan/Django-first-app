from django.urls import path
from . import views

urlpatterns = [
    path("helloworld", views.hello_world,name='helloWorld'),
    path("articles", views.article_list,name='articles'),
    path("<int:id>/", views.post,name='postById'),
    
]
