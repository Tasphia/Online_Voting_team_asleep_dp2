from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from .models import Nid_db

@csrf_protect
def verification_portal(request):
    return render(request, "index.html")

def NID_verification(request):
    if request.method == "POST":
        NID_no = request.POST['NID_no']

        try:
            user = Nid_db.objects.get(nid=NID_no)  # Try to get the user with that NID
            # Redirect to signup/login page after successful verification
            return redirect('signup')  # Redirect to signup page (change to the correct name)
        except Nid_db.DoesNotExist:
            return HttpResponse("Invalid NID. Please try again.")
    
    return render(request, 'login.html')

def dashboard(request):
    return render(request, "dashboard.html")

def success_page(request):
    return render(request, 'dashboard.html')  # Define the success page template




