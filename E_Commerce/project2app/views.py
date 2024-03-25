from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def shop(request):
    return render(request,'shop.html')
def detail(request):
    return render(request,'detail.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def contact(request):
    if request.method == 'POST':
        form = CustomerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added successfully')
        else:
            return HttpResponse(form.errors)
    else:
        form = CustomerDetailForm()
    return render(request, 'contact.html', {'form': form})
