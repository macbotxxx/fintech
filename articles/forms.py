from .models import My_Cars
from django import forms

class CarForm(forms.ModelForm):

    class Meta:
        model = My_Cars
        fields = '__all__'
        