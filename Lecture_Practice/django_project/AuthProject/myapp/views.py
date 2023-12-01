from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=signupdata.objects.filter(username=unm,password=pas)
        if user: #TRUE
            print("Login Successfull!")
        else:
            print("Error! Login Fail....")
    return render(request,'index.html')


def usersignup(request):
    if request.method=="POST":
        newuser=signupform(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("signup successfully...")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')