from django import forms
from .models import Resumé


class ResuméForm(forms.ModelForm):
    class Meta:
        model = Resumé
        fields = ('document',)