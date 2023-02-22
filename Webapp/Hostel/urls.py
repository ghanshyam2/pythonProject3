from django.urls import path
from . import views

urlpatterns = [

    path('',views.viewHostel, name= "viewHostel"),
    path('home/',views.home, name= 'home'),
    path('about/', views.aboutUs, name='about'),
    path('contact/', views.contactUs, name='contact'),

]