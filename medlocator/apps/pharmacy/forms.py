from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Pharmacy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    pharmacy_name = forms.CharField()
    account_manager_first_and_last_name = forms.CharField()
    account_manager_phone_number= forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Pharmacy
        fields = ('pharmacy_name','account_manager_first_and_last_name','account_manager_phone_number','email','password1','password2') 
