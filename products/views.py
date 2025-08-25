from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Products
import json

# Create your views here.
def index(request):
    products=Products.objects.all()
    return render(request,"products.html",{'products':products})

def product_detail(request,id,slug):
    products=get_object_or_404(Products,id=id,slug=slug)
    return render(request,"detail.html",{'products':products})

def search_view(request):
    if request.method=='POST':
        query=request.POST.get("query")
        results = []
        if query:
            results = Products.objects.filter(name__icontains=query)
        
        return render(request,"productsearch.html",{'query':query,'results':results})


@csrf_exempt
def add_products(request):
    if request.method=="POST":
        try:
            data = json.loads(request.body)
            
            preview=data.get("preview")
            name=data.get("name")
            fullname=data.get("fullname")
            os=data.get("os")
            featured=data.get("featured")
            certified=data.get("certified")
            modal=data.get("model")
            processor=data.get("processor")
            label=data.get("label")
            price=data.get("price")
            cprice=data.get("cprice")
            quantity=data.get("quantity")
            description=data.get("description")
            size=data.get("size")
            color=data.get("color")
            weight=data.get("weight")
            sellertype=data.get("sellertype")
            seller=data.get("seller")
            brand=data.get("brand")
            category=data.get("category")
            prime=data.get("prime")
            charge=data.get("charge")
            
            product = Products.objects.create(
                preview=preview,
                name=name,
                fullname=fullname,
                featured=featured,
                prime=prime,
                certified=certified,
                os=os,
                processor=processor,
                modal=modal,
                category=category,
                brand=brand,
                sellertype=sellertype,
                seller=seller,
                charge=charge,
                label=label,
                weight=weight,
                color=color,
                size=size,
                price=price,
                cprice=cprice,
                description=description,
                quantity=quantity
            )

            return JsonResponse({'status': 'success', 'message': 'Product created', 'product_id': product.id})
           
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400) 
        
        
        
    return JsonResponse({"success":True})