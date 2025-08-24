from django.urls import path
from orders import views
urlpatterns = [
    path("",views.index,name="orders"),
    path("create",views.create_order,name="create_order"),
    path("confirm",views.order_confirm,name="order_confirm"),
    path("update_address",views.UpdateAddress,name="update_order_info")
]