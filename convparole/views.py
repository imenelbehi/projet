from os import name

from django.shortcuts import render,redirect
from django.http import HttpRequest
from convparole.models import Convparole
import speech_recognition as sr
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='log')
def conversion_parole(request):


    return render(request,'convparole/conversion_parole.html',)
def validation (request):
    if request.method == 'POST':
        r = sr.Recognizer()
        rr = request.POST["select-file"]
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("dit quelque chose :")
        audio = r.listen(source)
        aud = request.POST["audio-control"]
        try:
            print("you have said : " + r.recognize_google(audio, language="fr-FR"))

        except Exception as e:
            print("Error : ")
            dict = {
                'rr': rr,
                'aud': aud
            }
    return render(request, 'convparole/validation.html',dict)





