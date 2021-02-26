from django.urls import path
from . import views

urlpatterns = [
    path('register', views.log_reg, name="register"),
    path('login', views.log_reg, name="login"),
    path('logout', views.logout, name="logout"),
]
