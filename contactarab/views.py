from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def view(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = contactForm()
    return render(request, 'arab/contactar.html', context={'form': form})