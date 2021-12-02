from typing import AbstractSet
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField

# Create your models here.

# class demo(models.Model):
#     name=models.CharField(max_length=10)

class User(AbstractUser):
    is_email_verified=models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Pet(models.Model):
    
    SEX_CHOICES = (
        ('Female', 'Female',),
        ('Male', 'Male',),
        
    )
    RACE_CHOICES=(
        ('Dog','Dog'),
        ('Cat','Cat'),
        ('Other','Other'),
    )
    PURPOSE_CHOICES=(
        ('Give','Give'),
        ('Breed','Breed'),
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
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    # user_favourite=models.ForeignKey(UserFavourite,on_delete=CASCADE,default=None,null=True,blank=True)
    # favourites=models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    def __str__(self):
        return self.name
    

class UserFavourite(models.Model):
        user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
        
class Comment(models.Model):
    # title=models.CharField(max_length=255)
    body=models.CharField(max_length=1000)
    pet =models.ForeignKey(Pet,on_delete=CASCADE,related_name='comments')
    postBy=models.ForeignKey(User,on_delete=CASCADE,related_name='postby')



# class Product(models.Model):    
#     name=models.CharField(max_length=20)
#     price=models.IntegerField()
#     quanntity=models.IntegerField()
    
