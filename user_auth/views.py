from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"signup.html")

def login_view(request):
    return render(request,"signin.html")

def dashboard(request):
    return render(request,"dashboard.html")
