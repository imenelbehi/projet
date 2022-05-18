from django.urls import path
from . import views


urlpatterns = [

    path('', views.conversion_texte,name='lecture_automatique'),
]