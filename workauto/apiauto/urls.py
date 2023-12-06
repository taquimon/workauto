from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('apiauto/', views.apiauto, name='apiauto'),
    path('all/', views.all, name='all'),
]