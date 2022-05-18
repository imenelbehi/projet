from django.urls import path
from . import views
from resumé import views

urlpatterns = [

    path('', views.textes_resumés,name='textes_resumés'),

]