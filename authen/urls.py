from django.urls import path
from . import views


urlpatterns = [

    path('', views.authentification,name='log'),
    path('quitter', views.logoutUser, name='quitter'),
]