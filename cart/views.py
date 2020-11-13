from django.shortcuts import render
from .models import Cart
def cartview(request):
    cartcon = Cart.objects.all()[0]
    return render(request, 'cart.html', context={'Cart': cartcon})