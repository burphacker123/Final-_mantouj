from django.shortcuts import render
from .models import HomeSliders
from blog.models import BlogClass
from artisanalProd.models import ArtisanalProd
from about.models import AboutObj
from homeProduct.models import HomeObj
# Create your views here.
def index(request):
    blogObj = BlogClass.objects.all()
    sliders = HomeSliders.objects.all()
    return render(request, 'fr/indexfr.html', context={'sliders': sliders, 'blog': blogObj, 'homeobj': choice})
def about(request):
    aboutObject = AboutObj.objects.all()
    return render(request, 'fr/aboutfr.html', context={"about": aboutObject})
def natural(request):
    prods = NaturalProd.objects.all()
    return render(request, 'fr/shopfr.html', context={"prods":prods})
def artisanal(request):
    prods = ArtisanalProd.objects.all()
    return render(request, 'fr/artisanalfr.html', context={"prods":prods})
def blog(request):
    blogObj = BlogClass.objects.all()
    return render(request, 'fr/blogfr.html', context={'blog': blogObj})