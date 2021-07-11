from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Pharmacy


# Create your views here.
def become_pharmacy(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            pharmacy = Pharmacy.objects.create(name=user.username, created_by=user)

            return  redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'pharmacy/become_pharmacy.html', {'form': form})
