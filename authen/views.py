from django.shortcuts import render,redirect
from django.http import  HttpRequest
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def authentification(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acc')
        else:
            messages.info(request,'il y a une erreure qui se produite')
    return render(request,'loginn/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('log')