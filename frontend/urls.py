from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contactus_page, name='contact')
]




