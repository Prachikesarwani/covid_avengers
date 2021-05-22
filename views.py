from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from .models import Register, Registerbtn
from django.contrib import messages
from django.forms import modelformset_factory
from django.template import loader
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    return render(request,'index.html')

def LINKS(request):
    return render(request,'links.html')
    
def COWIN(request):
    return render(request,'cowin.html')

def REGISTER(request):
    if request.method == "POST":
        form = Register(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
       
        REGISTER = Register(username=username,email=email,phone=phone,address=address,password=password,date=datetime.today())
        if form.is_valid():
           REGISTER.save()
           messages.success(request, 'You are registered to the website.')
           print(request.POST)

    return render(request,'index.html#REGISTER')   

def CONTACT(request):
    return render(request,'contact.html')

def registerbtn(request):
    return render(request,'new.html')   
    if request.method == "POST":
        form = Registerbtn(request.POST)
        Requirement = request.POST.get('Requirement')
        Quantity = request.POST.get('Quantity')
        registerbtn = Registerbtn(Requirement=Requirement,Quantity=Quantity)
        registerbtn.save()
        print(request.POST)

def tnc(request):
    return render(request,'tnc.html')

def thanks(request):
    return render(request,'thanks.html')

def SIGN(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = AuthenticationForm(username=username, password=password)
        if user is not None:
            login(request,user)
            # A backend authenticated the credentials
            return redirect("/new.html")    
        else:
            # No backend authenticated the credentials
             return render(request,'/index.html#sign')  

    return render(request,'index.html#sign')    


def logoutuser(request):
    logout(request)
    return redirect("/")
   