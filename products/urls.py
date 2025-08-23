from django.urls import path
from products import views

app_name= 'products'

urlpatterns = [
    path("",views.index,name="products"),
    path("add",views.add_products,name="add_products"),
    path("product/<int:id>/<slug:slug>",views.product_detail,name="product_details"),
    path("search",views.Search_view,name="search_products")
]
