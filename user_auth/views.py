from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,get_user_model,logout
User=get_user_model()
from django.contrib import messages
from eccomerce.middleware import auth

# Create your views here.
def register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        lastname=request.POST.get("lastname")
        firstname=request.POST.get("firstname")
        password=request.POST.get("password")
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"User Already Exists")
            return redirect('register')
        
        user=User.objects.create(
            email=email,
            phone=phone,
            first_name=firstname,
            last_name=lastname
        )
        
        user.set_password(password)
        user.save()
        
        return redirect("dashboard")
        
    return render(request,"signup.html")

def login_view(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        if not User.objects.filter(email=email).exists():
            messages.error(request,"User Does not Exists")
            return redirect('login')
        
        user=authenticate(username=email,password=password)
        
        if user is None:
            messages.error(request,"Invalid password")
            return redirect('login')
        else:
            login(request,user)
            return redirect("dashboard")
        
    return render(request,"signin.html")

@auth
def dashboard(request):
    return render(request,"dashboard.html")

@auth
def logout_view(request):
    logout(request)
    return redirect("login")
