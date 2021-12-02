from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Pet,Comment

class PetForm(forms.ModelForm):
    class Meta:
        model=Pet
        fields=('name','gender','age','race','type','purpose','location','image')
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        widgets={
            'body':forms.Textarea(attrs={'class': 'comment__body'}),
        }
        fields=('body',)