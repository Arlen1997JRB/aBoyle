from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView

def home(request):
	return render (request, 'reviews/home.html',{'title': 'home'}) 

def about(request):
	return render(request, 'reviews/about.html',{'title': 'about'})

def contact(request):
	return render(request, 'reviews/contact.html',{'title': 'contact'})

def product(request):
	product= {
		'products' : Product.objects.all()
	}
	return render(request, 'reviews/product.html',{'title': 'product'})

class ProductListView(ListView):
	model = Product
	template_name = 'reviews/products.html'
	object_context_name = 'product'
	ordering = ['-name']
# Create your views here.
