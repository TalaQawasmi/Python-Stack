from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('guess',views.guess),
    path('replay',views.replay),
]   