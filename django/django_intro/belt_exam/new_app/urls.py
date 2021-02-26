from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("register", views.register),
    path("success/<user_id>", views.success),
    path('log_in', views.log_in),
]