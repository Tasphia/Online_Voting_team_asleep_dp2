from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from .models import User

@csrf_protect

def login(request):
    return render(request,"index.html")

def NID_verification(request):
    if request.method=="POST":
        NID_no=request.POST['NID_no']

        try:
            user = User.objects.get(nid=NID_no)  # Try to get the user with that NID
            # If the NID exists, redirect to another page
            return redirect('success_page')  # Replace 'success_page' with the desired page
        except User.DoesNotExist:
            # If the NID doesn't exist, return an error message
            return HttpResponse("Invalid NID. Please try again.")
    
    return render(request, 'login.html')


def dashboard(request):
    return render(request,"dashboard.html")

def success_page(request):
    return render(request, 'success.html')  # Define the success page template




