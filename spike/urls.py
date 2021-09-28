from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from spike.views import Mainview
from spike import views

urlpatterns = [
    path('',views.images,name='images'),
    path('upload', Mainview.as_view(),name='upload'),
    path('Acedemi',views.academi,name='Acedemi'),
    path('Art',views.art,name='Art'),
    path('Buildings',views.buildings,name='Buildings'),
    path('Cars',views.cars,name='Cars'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]