from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model=Pet
        fields=('name','gender','age','race','type','purpose','location','image')