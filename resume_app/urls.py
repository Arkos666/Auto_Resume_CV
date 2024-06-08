from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.home, name='index'),
    path('tags', views.skills, name='skills'),
]