from django.shortcuts import render
from .models import ArtisanalProduct, HomeProducts, NaturalProduct, HomeSliders, AboutPage, Blog
# Create your views here.
def index(request):
    blog = Blog.objects.all()
    sliders = HomeSliders.objects.all()
    products = HomeProducts.objects.all()[0]
    return render(request, 'arab/indexar.html', context={'sliders': sliders, 'products': products, 'blog': blog})
def about(request):
    aboutDescription = AboutPage.objects.all()
    return render(request, 'arab/aboutar.html', context={'description': aboutDescription})
def natural(request):
    Products = NaturalProduct.objects.all()
    return render(request, 'arab/shopar.html', context={'products': Products})
def artisanal(request):
    Products = ArtisanalProduct.objects.all()
    return render(request, 'arab/artisanalar.html', context={'products': Products})
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'arab/blogar.html', context={'blog':blog})