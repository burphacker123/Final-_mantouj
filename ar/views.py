from django.shortcuts import render
from .models import ArtisanalProduct, HomeProducts, NaturalProduct, HomeSliders, AboutPage
# Create your views here.
def index(request):
    sliders = HomeSliders.objects.all()
    products = HomeProducts.objects.all()
    return render(request, 'arab/indexar.html', context={'sliders': sliders, 'products': products})
def about(request):
    aboutDescription = AboutPage.objects.all()
    return render(request, 'arab/aboutar.html', context={'description': aboutDescription})
def natural(request):
    Products = NaturalProduct.objects.all()
    return render(request, 'arab/shopar.html', context={'products': Products})
def artisanal(request):
    Products = ArtisanalProduct.objects.all()
    return render(request, 'arab/artisanalar.html', context={'products': Products})
def contact(request):
    return render(request, 'arab/contactar.html')