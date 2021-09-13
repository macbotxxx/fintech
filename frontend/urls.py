from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contactus_page, name='contact'),
    path('welcome', views.welcome, name = 'welcome'),
    path('cars', views.all_cars, name='cars'),
    path('cars-details/<int:id>/', views.get_car_detail, name='cars-details'),
    path('payment/', views.PaymentView.as_view(), name='payment'),

    path ('success', views.success, name='success'),
    path ('form/', views.my_cars, name='my-cars'),
]




