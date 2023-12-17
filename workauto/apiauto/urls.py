from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('apiauto/<md_content>', views.apiauto, name='apiauto'),
    path('all/', views.all, name='all'),
    path("<md_content>", views.markdown_content_view, name="markdown-content"),
]