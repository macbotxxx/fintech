from django.shortcuts import redirect, render
from django.views.generic.base import View
from articles.models import Blog, My_Cars
from django.contrib.auth.decorators import login_required
from articles.forms import CarForm
from balance.models import Transaction_history

import json
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


class PaymentView (View):
    def get(self, request, *args, **kwargs):
        trans1 =Transaction_history.objects.all()
        trans2 =Transaction_history.objects.filter(user_id = self.request.user)

        context = {
            'trans1':trans1,
            'trans2':trans2,
        }
        
        return render(request, 'pages/welcome.html', context)

    def post (self,request, *args, **kwargs):
        data = json.loads(self.request.body)
        status = data['status']
        transref = data['transref']
        amount = data['amount']
        currency = data['currency']

        Transaction_history.objects.create(
            user_id = self.request.user,
            order_id = transref,
            billing_name = 'Testing Class Payment',
            amount = amount,
            status = status,  
            )

        return redirect('success')

def success(request):

    return render(request, 'pages/success.html')


def my_cars (request):
    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }

    return render(request, 'pages/welcome.html', context)

