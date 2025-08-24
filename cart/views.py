from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from products.models import Products
from django.views.decorators.http import require_POST
from .models import Cart,CartItem
from django.contrib import messages
import json
from eccomerce.middleware import auth

# Create your views here.
def cart_view(request):
    cart_id=request.session.get("cart_id")
    cart=None
     
    if cart_id:
        cart=get_object_or_404(Cart,id=cart_id)
        
    if not cart or not cart.items.exists():
        cart=None
        
    return render(request,"cart.html",{"cart":cart})

@require_POST
def add_cart(request,product_id):
    cart_id=request.session.get("cart_id")
    
    if cart_id:
        try:
            cart=Cart.objects.get(id=cart_id)
            
        except Cart.DoesNotExist:
            cart=Cart.objects.create()
            
    else:
        cart=Cart.objects.create()
        request.session['cart_id']=cart.id
    
    product=get_object_or_404(Products,id=product_id)
    
    cart_item, created=CartItem.objects.get_or_create(cart=cart,product=product)
    
    if not created:
        cart_item.quantity+=1
        
    cart_item.save()
       
    return redirect("cart")

def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, id=product_id, cart=cart)
    item.delete()
    
    return redirect("cart")

def update_cart_item_quantity(request):
    if request.method == 'POST':
        try:
            data=json.loads(request.body)
            id=data.get("id")
            action=data.get("action")
            cart_item = CartItem.objects.get(id=id)
            
            if action=="increase":
                new_quantity=cart_item.quantity+1
                cart_item.update_quantity(new_quantity)
                
            if action=="descrease":
                new_quantity=cart_item.quantity-1
                cart_item.update_quantity(new_quantity)
            
            return JsonResponse({'success': True, 'quantity': new_quantity})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
   
    return JsonResponse("Invalid request", status=400)

def cart_total_distinct_items(request):
    try:
        cart_id = request.session.get('cart_id')
        cart = Cart.objects.get(id=cart_id)
        total_items = cart.items.count()
        return JsonResponse({'total_items': total_items})
    
    except Cart.DoesNotExist:
        return JsonResponse({'error': 'Cart not found'}, status=404)
    
@auth
def Delete_cart(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    del request.session["cart_id"]
    return redirect("/")