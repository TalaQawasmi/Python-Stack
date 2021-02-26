from django.shortcuts import render, redirect
import bcrypt
from . import models
from django.contrib import messages
import re
import datetime


def index(request):
    return render(request, 'index.html')


def validate_text(text, min_length=2):
    if text.isalpha == False:
        return 0
    elif len(text) < min_length:
        return 1
    elif len(text) > min_length:
        return 2


def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        if not models.is_duplicate_email(email):
            return 0
        return 1
    return 2


def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        errors = models.user_validator(
            request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        if validate_text(request.POST['fname']) == 2 and validate_text(request.POST['lname']) and validate_text(request.POST['password'], min_length=8) == 2 \
                and validate_email(request.POST['email']) == 0 and request.POST['password'] == request.POST['confirm']:
            user = models.insert_new_user(
                request.POST['fname'], request.POST['lname'], request.POST['email'], pw_hash, request.POST['date'])
            if 'user_id' not in request.session:
                request.session['user_id'] = user.id
            return redirect('/books')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = models.get_user(email)
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            if user is not None:
                print(user)
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                return redirect('/books')
    return redirect('/')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')


def books(request):
    context = {
        "all_books": models.all_books()
    }
    return render(request, "books.html", context)


def add_book(request):
    if request.method == 'POST':
        errors = models.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return('/books')
        book = models.insert_new_book(
            title=request.POST['title'], desc=request.POST['desc'], id=request.session['user_id'])
        return redirect('/books/'+str(book.id))


def book_profile(request, id):
    book = models.get_book(id)
    user = models.get_user_by_id(request.session['user_id'])
    liked_books = book.liked_books.all()
    context = {
        "book": book,
        "user": user,
        "liked_books": liked_books
    }
    return render(request, "book_profile.html", context)


def edit(request, id):
    edit = models.edit_book(id, request.POST)
    return redirect('/books/'+str(id))


def add_to_favorites(request, book_id, user_id):
    add = models.add_to_favorites(book_id, user_id)
    return redirect('/books/'+str(book_id))


def unfavorite(request, book_id, user_id):
    remove = models.remove_from_favorites(book_id, user_id)
    return redirect('/books/'+str(book_id))
