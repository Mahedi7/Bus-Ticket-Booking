from django.shortcuts import render
from django.db import models
from django.contrib import admin
from django.http import HttpResponse
from . models import SignUp
from . models import Bus
from . models import Passenger
from django.contrib import messages
def home(request):
    return render(request, 'first page.html')

def signup(request):
    if request.method == 'POST':
        FirstName = request.POST['First Name']
        LastName = request.POST['Last Name']
        UserName = request.POST['Username']
        Email = request.POST['email']
        Password = request.POST['psw']
        user = SignUp(First_Name=FirstName, Last_Name=LastName, User_Name=UserName, Email=Email, Password=Password)
        user.save()
        return render(request, 'search page.html')
    else:
        return render(request, 'sign up.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        UserName = request.POST['uname']
        Password = request.POST['psw']
        if UserName:
            match1 = SignUp.objects.filter(User_Name=UserName)
            if match1:
                if Password:
                    match2 = SignUp.objects.filter(Password=Password)
                    if match2:
                        return render(request, 'search page.html')
                    else:
                        messages.error(request, 'Invalid User Name or Password!')
                        return render(request, 'login page.html')
                else:
                    messages.error(request, 'Invalid User Name or Password!')
                    return render(request, 'login page.html')
            else:
                messages.error(request, 'Invalid User Name or Password!')
                return render(request, 'login page.html')
        else:
            messages.error(request, 'Invalid User Name or Password!')
            return render(request, 'login page.html')
    else:
        return render(request, 'login page.html')

def search(request):
        return render(request, 'search page.html')

def bus(request):
    return render(request, 'bus page.html')

def seat(request):
    return render(request, 'bus seat.html')

def passenger(request):
    return render(request, 'passenger.html')

def last(reqeust):
    return render(reqeust, 'Last page.html')

