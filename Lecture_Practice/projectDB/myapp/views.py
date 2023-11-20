from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def index(request):

    if request.method=="POST":
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        mob=request.POST['mobile']
        dob=request.POST['dob']
        add=request.POST['address']
        userinfo.objects.create(firstname=fnm,lastname=lnm,email=email,mobile=mob,dob=dob,address=add)
        print("your data has been inserted")
    else:
        print("error...")
    return render(request,"index.html")

def Showdata(request):
    data=userinfo.objects.all()
    return render(request,"Showdata.html",{'data':data})

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=="POST":
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        mob=request.POST['mobile']
        dob=request.POST['dob']
        #add=request.POST['address']
        userinfo.objects.filter(id=id).update(firstname=fnm,lastname=lnm,email=email,mobile=mob,dob=dob)
        return redirect("Showdata")
    else:
        print("error...Something went wrong...Try again!")
    return render(request,"updatedata.html",{'stid':stid}) #stid:stid means context
    

def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect("Showdata")





