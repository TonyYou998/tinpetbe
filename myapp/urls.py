from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('find',views.find,name="find"),
    path('breed',views.breed,name='breed'),
    path('give',views.give,name='give'),
    

]