from django.urls import path
from . import views


urlpatterns = [

    path('', views.contactPage,name='contact'),

]