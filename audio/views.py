from django.shortcuts import render, redirect
#pytub package for download youtube video
from pytube import YouTube
import os
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings as django_settings
import os
import wave
import speech_recognition as sr
import pyttsx3
from django.core.files.storage import default_storage
from .models import *
import speech_recognition as spr
from googletrans import Translator
from urllib import parse
import requests as requests
import re
import base64
r = sr.Recognizer()
# Create your views here.
def audioPage(request):
    # python3

    if request.is_ajax():
        print('a===>>>>>', request.GET.get('datas'))
        print('a===>>>>>', request.FILES.get('datas'))
        print('a===>>>>>', request.GET.get('datas'))

    if request.method == 'POST':
        file = request.FILES.get('file')
        lang = request.POST.get('lang')
        dlang = request.POST.get('dlang')
        aobj = Audio()
        aobj.audioname = 'temp1'
        aobj.audio = file
        aobj.save()
        # Using ggogle to recognize audio
        audio = Audio.objects.last()
        adurl = str(audio.audio.url)
        with spr.WavFile(adurl[1:]) as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language=dlang)
        translator = Translator()
        ttext = translator.translate(text, src=dlang, dest=lang)

        coded_string = request.POST.get('blobdata')

        sample_string_bytes = coded_string.encode("UTF-8")
        imgdata = base64.b64decode(sample_string_bytes)
        filename = 'some_image.wav'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)


    return render(request,'audio/audio.html')


