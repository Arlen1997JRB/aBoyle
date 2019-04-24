from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return render (request, 'reviews/home.html',{'title': 'home'}) 

def about(request):
	return render(request, 'reviews/about.html',{'title': 'about'})

def contact(request):
		return render(request, 'reviews/contact.html',{'title': 'contact'})

def product(request):
		return render(request, 'reviews/product.html',{'title': 'product'})
# Create your views here.
