from django.urls import path
from . import views

urlpatterns =[

path('', views.home, name='reviews-home'),
path('about/', views.about, name='reviews-about'),
path('contact/', views.about, name='reviews-contact'),
path('product/', views.about, name='reviews-product'),
path('profile/', views.about, name='reviews-profile'),

]

