from django.shortcuts import render, Http404
from .models import HomeSliders
from blog.models import BlogClass
from naturalProd.models import NaturalProd
from artisanalProd.models import ArtisanalProd
from about.models import AboutObj
from homeProduct.models import HomeObj
def index(request):
    choice = HomeObj.objects.all()[0]
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
def singlear(request, slug):
    try:
        product = ArtisanalProd.objects.get(slug = slug)
        return render(request, 'product-single.html', context={'product':product})
    except:
        raise Http404
def singlena(request, slug):
    try:
        product = NaturalProd.objects.get(slug = slug)
        return render(request, 'product-single.html', context={'product':product})
    except:
        raise Http404