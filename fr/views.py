from django.shortcuts import render
from .models import ArtisanalProduct, HomeProducts, NaturalProduct, HomeSliders, AboutPage
# Create your views here.
def index(request):
    sliders = HomeSliders.objects.all()
    products = HomeProducts.objects.all()[0]
    return render(request, 'fr/indexfr.html', context={'sliders': sliders, 'products': products})
def about(request):
    aboutDescription = AboutPage.objects.all()
    return render(request, 'fr/aboutfr.html', context={'description': aboutDescription})
def natural(request):
    Products = NaturalProduct.objects.all()
    return render(request, 'fr/shopfr.html', context={'products': Products})
def artisanal(request):
    Products = ArtisanalProduct.objects.all()
    return render(request, 'fr/artisanalfr.html', context={'products': Products})
def contact(request):
    return render(request, 'fr/contactfr.html')