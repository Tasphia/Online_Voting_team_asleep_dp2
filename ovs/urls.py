from django.contrib import admin
from django.urls import path
from . import views
from .views import SignUpView, LoginView, LogoutView  

urlpatterns = [
    path('', views.verification_portal, name='verification_portal'),
    path('NID_verification/', views.NID_verification, name='NID_verification'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/', views.success_page, name='success_page'),
]
