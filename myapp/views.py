from django import forms
from django import contrib
from django.contrib.auth import tokens,get_user_model
from django.forms.fields import EmailField
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from six import text_type
from .form import CommentForm, PetForm,CodeForm
from .models import Pet,Comment
from django.core.mail import send_mail,EmailMessage
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str,force_text,DjangoUnicodeDecodeError
# from utils import generate_token
from .utils import generate_token
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from tinpet.utils import send_sms


# Create your views here.
User=get_user_model()
def index(request):
    dogs=Pet.objects.all().filter(race="Dog").order_by("-id")[:8]
    
    cats=Pet.objects.all().filter(race="Cat").order_by("-id")[:8]

    return render(request,'index.html',{'dogs':dogs,'cats':cats})

def send_action_email(user,request):
    current_Site=get_current_site(request)
    email_subject='Activate your account'
    email_body=render_to_string('activate.html',{
            'user':user,
            'domain':current_Site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
    })
    email= EmailMessage(subject=email_subject,body=email_body ,from_email= settings.EMAIL_FROM_USER,to= [user.email])
    email.send()


    
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        print("phone"+phone)
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
                user.phone_number=phone
                user.save()
                
                send_action_email(user,request)
                messages.info(request,'Please check your email to verify')

                return redirect('register')
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
        if not user.is_email_verified:
            messages.info(request,"Email is not verify. Please verify your email")
            return   redirect('login')
        if user is not None:
            # auth.login(request,user)
            request.session['pk']=user.pk

           
            return redirect('verify_view')
        else:
            messages.info(request,'Username or Password are incrorect')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def activate_user(request,uidb64,token):
    try:
        print("run code in try")
        
        uid=force_text(urlsafe_base64_decode(uidb64))
        print("uid:",uid)
        user=User.objects.get(pk=uid)
        print("user:",user)

    except Exception as e:
         user=None
    
    if user and generate_token.check_token(user,token):
        user.is_email_verified=True
        user.save()
        messages.info(request,"Verified success")
        return redirect('login')
    return render(request,'authentication/activate-failed.html',{"user":user})

def find(request):
   
    if request.method=='GET':
        pet=Pet.objects.all().filter(purpose='Give')
        
        page_number=request.GET['page']
        pet_paginator=Paginator(pet,8)
        page=pet_paginator.get_page(page_number)
        
        return render(request,'find.html',{'pets':page})
    else:
        name=request.POST['name']
        race=request.POST['race']
        print(name,race)
        if race=="" or race=="A":
            
            pet=Pet.objects.all().filter( purpose='G',name=name)
            print(pet)
        elif name=="":
             pet=Pet.objects.all().filter( purpose='G',race=race)
       
        else :
            pet=Pet.objects.all().filter( purpose='G',name=name,race=race)
            pet_paginator=Paginator(pet,8)
            page=pet_paginator.get_page(1)
   
    return render(request,'find.html',{'pets':page})
    

   

def breed(request):
    if request.method=='GET':
        pet=Pet.objects.all().filter(purpose='Breed')
        page_number=request.GET['page']
        pet_paginator=Paginator(pet,8)
        page=pet_paginator.get_page(page_number)
        print("pet:",pet)
        return render(request,'breed.html',{'pets':page})
    else:
        name=request.POST['name']
        race=request.POST['race']
        
        if race=="" or race=="A":
            
            pet=Pet.objects.all().filter( purpose='B',name=name)
       
        elif name=="":
             pet=Pet.objects.all().filter( purpose='B',race=race)
       
        else :
            pet=Pet.objects.all().filter( purpose='B',name=name,race=race)
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
    comment=Comment.objects.all().filter(pet=pet)
    # print(comment[0].body)
    form=CommentForm();
    return render(request,'detail.html',{'pet':pet,'form':form,'comment':comment})
def send(request):
    email=request.GET['email']
    userMail=request.GET['owner']
   
    message='hello this email to inform you that '+userMail+ " would like to adopt your pet. please contact with him/her."
   
    send_mail('About your pet on tinpet',message,'tinpetofficial@outlook.com',[email], fail_silently=False)
    messages.info(request,'Email has been sent')
    return redirect('/')
    
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
def editUser(request,pk):
    
    if request.method=='POST' and request.user.is_authenticated:
        username=request.POST['username']
        email=request.POST['email']
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        
        user=User.objects.get(id=pk)
        if user.username != username:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already used')
                return redirect('/profile')
        user.username=username
        user.email=email
        user.first_name=firstName
        user.last_name=lastName
        user.save()
        return redirect("/profile")
    else:
        return redirect('/')
def addToFavourite(request,pk):
   
    pet=Pet.objects.get(id=pk)
    print(pet)
    # if pet.favourites.filter(id=request.user.id).exists():
        # pet.favourites.remove(request.user)
    # else:
    pet.favourites.remove(request.user)
    # return redirect('detail/'+pk)
    return redirect("/")
def comment(request):
    
    
    if request.method=='POST':
        id=request.POST['id']
        pet=Pet.objects.get(id=id)
        
    
        form=CommentForm(request.POST)
        
        if form.is_valid():
            
            comment=form.save(commit=False)
            comment.pet=pet
            comment.postBy=request.user
            comment.save()
    return redirect('/detail/'+id)
# @login_required
# def home_view(request):
#     return render(request,'main.html',{})
# def auth_view(request):
#     form=AuthenticationForm()
#     if request.method=='POST':
#         username=request.POST.get('usuername')
        
def verify_view(request):
    form=CodeForm(request.POST or None)
    pk=request.session.get('pk')
    if pk:
        user=User.objects.get(pk=pk)
        code=user.code
        code_user=f"{user.username}:{user.code}"
        if not request.POST:
            # send sms
            print("code:"+code_user)
            print("phone",user.phone_number)
            send_sms(code_user,user.phone_number)
        if form.is_valid():
            num=form.cleaned_data.get('number')

            if str(code)==num:
                code.save()
                auth.login(request,user)
                return redirect('/')
            else:
                 return redirect('/login')
    return render(request,'verify.html',{'form':form})
        
    

    