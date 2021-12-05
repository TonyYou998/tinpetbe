from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Pet,Comment,Code

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

class CodeForm(forms.ModelForm):
    number=forms.CharField(label='Code',help_text='enter sms verifycation code')
    class Meta:
        model=Code
        fields=('number',)