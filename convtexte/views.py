from django.shortcuts import render
import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
# Create your views here.
@login_required(login_url='log')
def conversion_texte(request):
    language= 'en'
    if request.method == 'POST':
        book = askopenfilename()
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages
        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            player = pyttsx3.init()
            player.say(text)
            player.runAndWait()

    return render(request,'convtexte/conversion_texte.html')
