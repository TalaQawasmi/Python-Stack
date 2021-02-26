from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('travels', views.dashboard, name="dashboard"),
    path('travels/destination/<int:id>', views.destination, name="destination"),
    path('travels/add', views.add_page, name='add_page'),
    path('travels/add/trip', views.add, name="add"),
    path('travels/join/<int:id>', views.join, name='join'),
]
