from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('shop', views.natural, name='natural'),
    path('artisanal', views.artisanal, name='artisanal')    
]