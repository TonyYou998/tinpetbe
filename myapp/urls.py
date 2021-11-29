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
    path('detail/<int:pk>',views.detail,name='detail'),
    path('send',views.send,name='send'),
    path('profile',views.profile,name='profile'),
    path('mypet',views.mypet,name='mypet'),
    path('mypet/delete/<int:pk>',views.deletePet,name='deletePet'),
    path('editpet/<int:pk>',views.editPet,name='editPet'),
    path('edituser/<int:pk>',views.editUser,name='editUser')
    

]