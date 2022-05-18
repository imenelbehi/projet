from django.urls import path
from . import views


urlpatterns = [

    path('', views.conversion_parole,name='convertir_en_texte'),
    path('validate', views.validation, name = 'validation')

]