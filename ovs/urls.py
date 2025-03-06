from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.login,name='login'),
    path('NID_verification', views.NID_verification, name='login_view'),
    path('success', views.success_page, name='success_page'),
   path('dashboard.html',views.dashboard,name='dashboard')
   
]
