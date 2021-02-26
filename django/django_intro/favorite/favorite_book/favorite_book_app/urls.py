from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_user', views.register),
    path('login', views.login),
    path('add_book', views.add_book),
    path('books', views.books),
    path('books/<int:id>', views.book_profile),
    path('logout', views.logout),
    path('edit/<int:id>', views.edit),
    path('add_to_favorites/<int:book_id>/<int:user_id>', views.add_to_favorites),
    path('unfavorite/<int:book_id>/<int:user_id>', views.unfavorite)
]
