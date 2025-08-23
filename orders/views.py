from django.shortcuts import render
from eccomerce.middleware import auth
# Create your views here.
@auth
def index(request):
    return render(request,"order.html")