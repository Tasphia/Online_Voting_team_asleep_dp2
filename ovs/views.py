from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout  
from .models import Nid_db, User
from .forms import SignUpForm, LoginForm

@csrf_protect
def verification_portal(request):
    return render(request, "index.html")

def NID_verification(request):
    """ Verify NID and redirect to signup page """
    if request.method == "POST":
        NID_no = request.POST['NID_no']

        try:
            user = Nid_db.objects.get(nid=NID_no)  # Check if NID exists
            return redirect('signup')  # Redirect to signup page
        except Nid_db.DoesNotExist:
            return HttpResponse("Invalid NID. Please try again.")
    
    return render(request, 'login.html')

def dashboard(request):
    """ Display Dashboard After Login """
    return render(request, "dashboard.html")


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            nid = form.cleaned_data['nid']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(nid=nid, password=password)  # ⚠ Checking plain-text password
                request.session['user_id'] = user.id  # Store user session
                return redirect('dashboard')  # ✅ Redirect to Dashboard after login
            except User.DoesNotExist:
                return HttpResponse("Invalid NID or Password")

        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        request.session.flush()  # Clear session data
        return redirect('verification_portal')  # Redirect to Home Page

def success_page(request):
    return render(request, 'success.html')  # Ensure 'success.html' exists in templates

