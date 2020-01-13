from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='shophome'),
   path('about/',views.about, name='about Us'),
   path('contact/',views.contact, name='contact Us'),
   path('tracker/', views.tracker, name='Tracking Status'),
   path('search/', views.search, name='Search'),
   path('product/', views.product, name='Product View'),
   path('checkout/', views.checkout, name='Checkout'),
]