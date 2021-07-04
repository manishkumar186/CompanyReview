from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect("reviewapp:home")
    else:
        if request.method == "POST":
            uname = request.POST["uname"]
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["eaddress"]
            psd = request.POST["pwd"]

            obj = User.objects.create_user(uname,email,psd)
            obj.first_name=fname
            obj.last_name=lname

            obj.save()
            return redirect("reviewapp:home")

        return render(request,"register.html")

def login_user(request):
    if request.user.is_authenticated:
        return redirect("reviewapp:home")
    else:
        if request.method == "POST":
            username = request.POST["uname"]
            password = request.POST["pwd"]

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("reviewapp:home")
                else:
                    return render(request,"login_user.html",{"error":"Your account has been suspended"})
            else:
                return render(request,"login_user.html",{"error":"Invalid username or password. Try Again."})
        return render(request,"login_user.html")


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("reviewapp:home")
    else:
        return redirect("reviewapp:home")
        
        
