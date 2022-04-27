from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'users/home.html')

def about(request):
    return render(request,'users/about.html')


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup.html', {'form': form})

def login(request):
    return render(request,'users/login.html')

def agriculture(request):
    return render(request, 'users/agriculture.html')


def childcare(request):
    return render(request, 'users/childcare.html')


def education(request):
    return render(request, 'users/education.html')


def healthcare(request):
    return render(request, 'users/healthcare.html')


def help(request):
    return render(request,'users/help.html')


def wildlife_1(request):
    return render(request, 'users/wildlife_1.html')


def wildlifenecology(request):
    return render(request, 'users/wildlifenecology.html')


def womendev(request):
    return render(request,'users/womendev.html')