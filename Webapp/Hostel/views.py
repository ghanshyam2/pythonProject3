from django.shortcuts import render

from django.http import HttpResponse


def viewHostel(request):
    data = {'title': 'Vidya Girls Hostel | Varanasi'}
    return render(request, 'index.html', data)


def home(request):
    return render(request, 'home.html')


def aboutUs(request):
    return render(request, 'about.html')


def contactUs(request):
    return render(request,'contact.html')
