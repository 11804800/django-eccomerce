from django.urls import path
from user_auth import views

urlpatterns = [
    path("login",views.login_view,name="login"),
    path("register",views.register,name="register"),
    path("dashboard",views.dashboard,name="dashboard")
]