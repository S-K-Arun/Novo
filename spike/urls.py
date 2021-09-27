from django.contrib import admin
from django.urls import path
from spike.views import Mainview
from spike import views

urlpatterns = [
    path('',views.images,name='images'),
    path('upload', Mainview.as_view(),name='upload'),
    path('Acedemi',views.academi,name='Acedemi'),
    path('Art',views.art,name='Art'),
    path('Buildings',views.buildings,name='Buildings'),
    path('Cars',views.cars,name='Cars'),

]