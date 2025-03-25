from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm
from .models import User_db

# Home Page
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

# Sign Up View
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # ⚠ Directly saving password as plain text
            return redirect('login')
        return render(request, 'users/signup.html', {'form': form})

# Login View
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            nid = form.cleaned_data['nid']
            password = form.cleaned_data['password']

            try:
                User_db = User_db.objects.get(nid=nid, password=password)  # ⚠ Checking plain-text password
                return redirect('home')  # Redirect to homepage after login
            except User_db.DoesNotExist:
                return HttpResponse("Invalid NID or Password")

        return render(request, 'users/login.html', {'form': form})

