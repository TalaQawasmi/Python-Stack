from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('addTrip', views.create),
    path('add',views.index),
    path('destination/<int:trip_id>',views.show)
]