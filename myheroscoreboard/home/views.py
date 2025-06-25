from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import ApprovedStudent

def index(request):
    if request.method == 'POST':
        if 'login_submit' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('dashboard')  # Make sure 'dashboard' is defined in urls.py
            else:
                messages.error(request, "Invalid login credentials")
        
        elif 'signup_submit' in request.POST:
            admissionNumber = request.POST.get('admissionNumber')
            email = request.POST.get('email')
            password = request.POST.get('signupPassword')

            # ✅ FIXED: Correct field name in ApprovedStudent
            try:
                ApprovedStudent.objects.get(admissionNumber=admissionNumber, email=email)
            except ApprovedStudent.DoesNotExist:
                messages.error(request, "Not authorized to register.")
                return redirect('home')  # Ensure 'home' exists in urls.py

            if User.objects.filter(username=admissionNumber).exists():
                messages.error(request, "User already exists.")
                return redirect('home')

            user = User.objects.create_user(username=admissionNumber, email=email, password=password)
            # ✅ FIXED: Use correct field names for Django User model
            user.first_name = request.POST.get('firstName')
            user.last_name = request.POST.get('lastName')
            user.save()
            messages.success(request, "Signup successful. Please log in.")
            return redirect('home')

    return render(request, 'index.html')
