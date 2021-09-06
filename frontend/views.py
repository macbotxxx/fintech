from django.shortcuts import render
from django.views.generic.base import View
from articles.models import Blog, My_Cars
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request):
    """
    Welcome home page for our fintech application.
    frontend -- 
    """
    all_post = Blog.objects.all()


    context = {
        'all_post':all_post,
    }
    return render(request, 'pages/index.html', context)


def contactus_page (request):
    """
    This is the contact us page for our fintech application.
    """
    
    return render(request, 'pages/contactus.html')
    

@login_required()
def welcome (request):
    """
    This is the contact us page for our fintech application.
    """
    
    return render(request, 'users_pages/index.html')

def all_cars (request):
    all_cars = My_Cars.objects.all()
    print(all_cars)
    context = {
        'all_cars': all_cars,
    }
    return render(request, 'pages/car.html', context)

def get_car_detail (request, id):
    all_cars = My_Cars.objects.filter(id = id)
  
    context = {
        'all_cars': all_cars,
    }
    return render(request, 'pages/car-detail.html', context)


    