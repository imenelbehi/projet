from django.urls import path
from . import views


urlpatterns = [

    path('', views.consulter_documentation,name='doc'),

]