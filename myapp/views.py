from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .form import PetForm
from .models import Pet
# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'check your password again')
            return redirect('register')

    else :
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
           
            return redirect('/')
        else:
            messages.info(request,'Username or Password are incrorect')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def find(request):
    pet=Pet.objects.all().filter(purpose='G')

    return render(request,'find.html',{'pets':pet})
def breed(request):
    return render(request,'breed.html')


def give(request):
    if request.method=="POST":
        form=PetForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            # gán name
            user=request.user
            name=user.username
            
          
            obj.owner=name
            obj.save()
            messages.info(request,'upload success')
            return redirect('give')
        else:
            messages.info(request,'upload failed')
            return redirect('give')
    else:
        form=PetForm()
        # pet=Pet.objects.all()
        return render(request,'give.html',{'form':form})