from django.shortcuts import render
from django.http import  HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='log')
def home(request):
    return render(request,'app/accueil.html')