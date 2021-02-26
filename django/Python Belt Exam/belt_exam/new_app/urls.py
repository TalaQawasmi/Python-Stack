from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
    path('quotes',views.quotes),
    path('create',views.create),
    path('add_favorite/(<id>)',views.add_favorite),
    path('remove_favorite/(<id>)',views.remove_favorite),
    path('users/(<id>)',views.show_user),
]