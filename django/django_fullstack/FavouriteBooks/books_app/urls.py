from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
]