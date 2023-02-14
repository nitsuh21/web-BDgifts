from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('gallery',views.gallery,name='gallery'),
    path('wishes',views.wishes,name='wishes'),
    path('videos',views.videos,name='videos'),
    path('makeawish',views.makeawish,name='makeawish'),
    path('giveagift',views.giveagift,name='giveagift'),
    path('login',views.login,name='login'),
    path('mygifts',views.mygifts,name='mygifts'),
    path('gifts/gift/<str:name>/',views.opengift,name='opengift'),
    path('contactus',views.contactus,name='contactus'),
]

