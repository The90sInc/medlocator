from django.contrib.auth.models import User, AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Pharmacy(AbstractBaseUser):
    pharmacy_name = models.CharField(max_length=250)
    Account_manager_first_and_last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=60, help_text='Required. Add a valid email')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='pharmacy', on_delete=models.CASCADE)
    Account_manager_phone_number = PhoneNumberField()


    USERNAME_FIELD = 'pharmacy_name'
    #REQUIRED_FIELDS = ['username', ]
    class Meta:
        ordering = ['pharmacy_name']

    def __str__(self):
        return self.pharmacy_name

