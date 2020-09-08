from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def natural(request):
    return render(request, 'shop.html')
def artisanal(request):
    return render(request, 'artisanal.html')
def contact(request):
    return render(request, 'contact.html')