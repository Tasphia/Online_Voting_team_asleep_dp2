from django.contrib import admin
from django.urls import path, include
from . import views
from .views import NID_verification
from users.views import SignUpView, LoginView  # Import views from users app

urlpatterns = [
    path('', views.verification_portal, name='verification_portal'),
    path('NID_verification/', views.NID_verification, name='NID_verification'),  # Fixed path
    path('signup/', SignUpView.as_view(), name='signup'),  # Use class-based view
    path('login/', LoginView.as_view(), name='login'),  # Fixed login path
    path('success/', views.success_page, name='success_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
]