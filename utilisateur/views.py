from django.shortcuts import render

from django.http import HttpRequest
# Create your views here.
def list_utilisateur(request):
    return render(request, 'utilisateur/list_utilisateur.html')
