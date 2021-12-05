from typing import AbstractSet
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.deletion import CASCADE
# from django.db.models.expressions import Random
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
import random
from twilio.rest import Client
# Create your models here.

# class demo(models.Model):
#     name=models.CharField(max_length=10)
# class Score(models.Model):
#     result=models.PositiveIntegerField()
#     def __str__(self):
#         return str(self.result)
#     def save(self,*args,**kwargs):
#         if self.result<70:
#             account_sid = 'AC96f5105aff90abe7ce797c607ef80e24'
#             auth_token = '7c95d518d085d309d71128a4e03a815c'
#             client = Client(account_sid, auth_token)

#             message = client.messages.create(
#                                 body="Hi,you has logged in to Tinpet this is your verifycation code: ",
#                                 from_='+12183040773',
#                                 to='+84368510465'
#                             )

#             print(message.sid)
#             return super().save(*args,**kwargs)
class User(AbstractUser):
    is_email_verified=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=12,default=None,null=True)

    def __str__(self):
        return self.email
class Code(models.Model):
    number=models.CharField(max_length=5,blank=True)
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number)
    def save(self,*args,**kwargs):
        number_list=[x for x in range(10)]
        code_items=[]
        for i in range(5):
            num=random.choice(number_list)
            code_items.append(num)
        code_string="".join(str(item) for item in code_items)
        self.number=code_string

        super().save(*args,**kwargs)

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
    
