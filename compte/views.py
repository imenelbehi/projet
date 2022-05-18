from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='log')
def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compte créé avec succès pour '+user)
            return redirect('log')
        else:
            messages.info(request,'utilisateur ou mot de passe introuvable')
    context={'form':form}
    return render(request,'compte/inscription.html',context)
