from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .models import Asset

def home(request):
    assets = Asset.objects.all()
    return render(request, 'home.html', {'assets': assets})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been successfully logged in !"))
            return redirect('home')
        else:
            messages.success(request, ("Something went wrong, please try again !"))
            return redirect('login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully !"))
    return redirect('home')

def signin_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # print("------>",request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, ("You have been signed in successfully !"))
            return redirect('login')
            
        else:
            print("Form Errors: ", form.errors) 
            messages.success(request, ("Something went wrong, please try again !"))
            return redirect('signin')
        
    return render(request, 'signin.html', {'form':form})
    

def image_gallery(request):

    images_row_1 = [
        {"url": "/image/1/", "src": "/static/images/image1.jpg", "alt": "Image 1", "details": "Image 1 Details"},
        {"url": "/image/2/", "src": "/static/images/image2.jpg", "alt": "Image 2", "details": "Image 2 Details"},
        {"url": "/image/3/", "src": "/static/images/image3.jpg", "alt": "Image 3", "details": "Image 3 Details"},
        {"url": "/image/4/", "src": "/static/images/image4.jpg", "alt": "Image 4", "details": "Image 4 Details"},
    ]

    context = {
        'images_row_1': images_row_1,
    }
    return render(request, 'image_gallery.html', context)

def collection(request):
    return render(request, 'collection.html')

def asset(request, pk):
    asset = Asset.objects.get(id = pk)
    return render(request, 'asset.html', {'asset': asset})
