from django.shortcuts import render
from .models import AboutPage, HomeProducts, HomeSliders, ArtisanalProduct, NaturalProduct

# Create your views here.
def index(request):
    sliders = HomeSliders.objects.all()
    products = HomeProducts.objects.all()[0]
    return render(request, 'index.html', context={'sliders': sliders, 'products': products})
def about(request):
    aboutDescription = AboutPage.objects.all()
    return render(request, 'about.html', context={'description': aboutDescription})
def natural(request):
    Products = NaturalProduct.objects.all()
    return render(request, 'shop.html', context={'products': Products})
def artisanal(request):
    Products = ArtisanalProduct.objects.all()
    return render(request, 'artisanal.html', context={'products': Products})
