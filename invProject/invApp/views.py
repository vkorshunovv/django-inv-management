from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

#Home View
def home_view(request):
    return render(request, 'invApp/home.html')

#Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return redirect(request, 'invApp/product_form.html', {'form': form})
    