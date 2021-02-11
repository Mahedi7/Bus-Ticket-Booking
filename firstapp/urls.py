from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'home', views.home, name='home'),
    path(r'signup', views.signup, name='signup'),
    path(r'contact', views.contact, name='contact'),
    path(r'about', views.about, name='about'),
    path(r'login', views.login, name='login'),
    path(r'search', views.search, name='search'),
    path(r'bus', views.bus, name='bus'),
    path(r'seat', views.seat, name='seat'),
    path(r'passenger', views.passenger, name='passenger'),
    path(r'last', views.last, name='last'),
]