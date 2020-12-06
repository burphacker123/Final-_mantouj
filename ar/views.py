from django.shortcuts import render
from .models import HomeSliders
from blog.models import BlogClass
from artisanalProd.models import ArtisanalProd
from about.models import AboutObj
from homeProduct.models import HomeObj
def index(request):
    choice = HomeObj.objects.all()
    blogObj = BlogClass.objects.all()
    sliders = HomeSliders.objects.all()
    return render(request, 'arab/indexar.html', context={'sliders': sliders, 'blog': blogObj, 'homeobj': choice})
def about(request):
    aboutObject = AboutObj.objects.all()
    return render(request, 'arab/aboutar.html', context={"about": aboutObject})
def natural(request):
    prods = NaturalProd.objects.all()
    return render(request, 'arab/shopar.html', context={"prods":prods})
def artisanal(request):
    prods = ArtisanalProd.objects.all()
    return render(request, 'arab/artisanalar.html', context={"prods":prods})
def blog(request):
    blogObj = BlogClass.objects.all()
    return render(request, 'arab/blogar.html', context={'blog': blogObj})