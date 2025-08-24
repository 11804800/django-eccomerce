from django.shortcuts import render,redirect,get_object_or_404
from eccomerce.middleware import auth
from products.models import Products
from cart.models import Cart
from .models import Order,OrderItem

@auth
def index(request):
    try:
        order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        order = None

    return render(request,"order.html",{'order':order})

@auth
def order_confirm(request):
    cart_id=request.session.get("cart_id")
    cart=None
     
    if cart_id:
        cart=Cart.objects.get(id=cart_id)
    if not cart or not cart.items.exists():
        cart=None
        return redirect("cart")
    
    if request.method=="POST":
        order, created = Order.objects.get_or_create(user=request.user)   
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
        
        return render(request,"order_success.html",{"cart":cart})
        
    return render(request,"order_confirm.html",{"cart":cart})

@auth
def create_order(request):
    cart_id=request.session.get("cart_id")
    cart=None
    
    if cart_id:
        cart=Cart.objects.get(id=cart_id)
        
        if not cart or not cart.items.exists():
            return redirect("cart")
        
    if request.user.address is None:
        if request.method=='POST':
            user = request.user
            user.address = request.POST.get('address')
            user.city = request.POST.get('city')
            user.state=request.POST.get("state")
            
            try:
                user.save()
                return redirect('order_confirm') 
            except Exception as e:
                return render(request,"order_create.html")
            
        return render(request,"order_create.html")
    
    else:
        return redirect('order_confirm')
    
@auth
def UpdateAddress(request):
    if request.method=='POST':
            user = request.user
            user.address = request.POST.get('address')
            user.city = request.POST.get('city')
            
            try:
                user.save()
                return redirect('order_confirm') 
            except Exception as e:
                return render(request,"order_create.html")
            
    return render(request,"order_create.html")