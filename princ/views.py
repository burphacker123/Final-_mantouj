from django.shortcuts import render
from .models import HomeSliders
from blog.models import BlogClass
from naturalProd.models import NaturalProd
from artisanalProd.models import ArtisanalProd
from about.models import AboutObj
from homeProduct.models import HomeObj
def index(request):
    choice = HomeObj.objects.all()
    blogPosts = BlogClass.objects.all()
    sliders = HomeSliders.objects.all()
    return render(request, 'index.html', context={'sliders': sliders, 'blog':blogPosts, 'homeobj': choice})
def about(request):
    aboutObject = AboutObj.objects.all()
    return render(request, 'about.html', context={"about": aboutObject})
def natural(request):
    prods = NaturalProd.objects.all()
    return render(request, 'shop.html', context={"prods":prods})
def artisanal(request):
    prods = ArtisanalProd.objects.all()
    return render(request, 'artisanal.html', context={"prods":prods})
def blog(request):
    blogPosts = BlogClass.objects.all()
    return render(request, 'blog.html', context={'blog': blogPosts})