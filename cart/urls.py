from django.urls import path
from cart import views

name="cart"
urlpatterns = [
    path("",views.cart_view,name="cart"),
    path("add/<int:product_id>",views.add_cart,name="add_cart"),
    path("update_quantity",views.update_cart_item_quantity,name="update_quantity"),
    path("remove_cart/<int:product_id>",views.cart_remove,name="remove_cart"),
    path("total_items",views.cart_total_distinct_items,name="total_items"),
    path("delete_cart",views.Delete_cart,name="delete_Cart")
]
