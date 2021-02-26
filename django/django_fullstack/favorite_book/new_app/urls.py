from django.urls import path
from . import views, models

urlpatterns = [
    path('',views.index),
    path('register',views.registration),
    path('success',views.success),
]