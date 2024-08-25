from django.contrib import admin
from django.urls import path
from authncon import views

urlpatterns =[
path('login',views.loginv,name='login'),
path('',views.Register,name='Register'),
path('dashboard',views.dashboard,name='DB'),
path('logout',views.logoutv,name='logout'),

]