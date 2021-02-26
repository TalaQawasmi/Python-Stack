from django.urls import path
from . import views, models

urlpatterns = [
    path('', views.index),
    path("register", views.registeration),
    path("success/<user_id>", views.success),
    path('log_in', views.log_in),
]