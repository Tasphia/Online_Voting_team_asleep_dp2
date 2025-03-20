from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.verification_portal,name='verification_portal'),
    path('NID_verification', views.NID_verification, name='login_view'),
    path('success', views.success_page, name='success_page'),
   path('dashboard.html',views.dashboard,name='dashboard')
   
]
