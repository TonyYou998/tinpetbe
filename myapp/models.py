from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# class demo(models.Model):
#     name=models.CharField(max_length=10)


class Pet(models.Model):
    
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        
    )
    RACE_CHOICES=(
        ('D','Dog'),
        ('C','Cat'),
        ('O','Other'),
    )
    PURPOSE_CHOICES=(
        ('G','Give'),
        ('B','Breed'),
    )
    name=models.CharField(max_length=20)
    gender=models.CharField(
         max_length=6,
        choices=SEX_CHOICES,
    )
    age=models.PositiveIntegerField()
   
    race=models.CharField(
        max_length=6,
        choices=RACE_CHOICES,
    )
    type=models.CharField(max_length=20)
    purpose=models.CharField(
        max_length=6,
        choices=PURPOSE_CHOICES,
    )
    location=models.CharField(max_length=20)
    image=models.ImageField(upload_to='img/%y')
    owner=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# class Product(models.Model):    
#     name=models.CharField(max_length=20)
#     price=models.IntegerField()
#     quanntity=models.IntegerField()
    
