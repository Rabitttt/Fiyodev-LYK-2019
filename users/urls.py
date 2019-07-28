"""
from django.contrib import admin
from django.urls import path,include
from .views import RegisterCBS
urlpatterns = [
    path('register',RegisterCBS.as_view(),name='register'),
    #path('ch/register/<int:pk>',CharacterRegister.as_view(),name='character_register'),


]
"""