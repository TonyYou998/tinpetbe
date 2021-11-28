from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .form import PetForm
from .models import Pet
from django.core.mail import send_mail
# Create your views here.

def index(request):
    dogs=Pet.objects.all().filter(race="D").order_by("-id")[:8]
    cats=Pet.objects.all().filter(race="C").order_by("-id")[:8]

    return render(request,'index.html',{'dogs':dogs,'cats':cats})


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
   
    if request.method=='GET':
        pet=Pet.objects.all().filter(purpose='G')
        return render(request,'find.html',{'pets':pet})
    else:
        name=request.POST['name']
        race=request.POST['race']
        return redirect('/')
    

   

def breed(request):
    pet=Pet.objects.all().filter(purpose='B')
    return render(request,'breed.html',{'pets':pet})



def give(request):
    if request.method=="POST":
        form=PetForm(data=request.POST,files=request.FILES)
        if form.is_valid():
        
            obj=form.instance
            # gán name
            user=request.user
            name=user.username
            email=user.email
            obj.email=email
            obj.user_id=request.user    
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
def detail(request,pk):
    pet=Pet.objects.get(id=pk)

    return render(request,'detail.html',{'pet':pet})
def send(request):
    email=request.GET['email']
    userMail=request.GET['owner']
   
    message='hello this email to inform you that '+userMail+ " would like to adopt your pet. please contact with him/her."
   
    send_mail('About your pet on tinpet',message,'tinpetofficial@outlook.com',[email], fail_silently=False)
    alert="email has been sent"
    return redirect('/',{'alert':alert})
    
def profile(request):
    userName=request.user

    numberOfPets=Pet.objects.filter(user_id=userName).count()
    # print('numberOfPets:',numberOfPets)
    return render(request,'info.html',{'number':numberOfPets})
def mypet(request):
   
    if (request.user.is_authenticated):
       
        username=request.user
        myPets=Pet.objects.all().filter(user_id=username)
        return render(request,'mypet.html',{'mypets':myPets})
    
    else:
         return redirect('/')


def deletePet(request,pk):
     
    if request.user.is_authenticated :

        Pet.objects.filter(id=pk).delete()

        return redirect('/mypet')
    return redirect('/')
def editPet(request,pk):
    
    if request.method=='POST' and request.user.is_authenticated:
        name=request.POST['name']
        age=request.POST['age']
        type=request.POST['type']
        location=request.POST['location']
        
        mypet=Pet.objects.get(id=pk)
        mypet.name=name
        mypet.age=age
        mypet.type=type
        mypet.location=location
        mypet.save()
        return redirect("/mypet")
    else:
        return redirect('/')