from django.urls import path     
from . import views
urlpatterns = [
    path('',views.index),
    path('game',views.game),
    path('restart',views.restart)
    ]