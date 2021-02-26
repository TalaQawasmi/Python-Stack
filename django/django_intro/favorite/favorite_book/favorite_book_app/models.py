from django.db import models
from . import views


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    books_uploaded = models.ForeignKey(
        User, related_name="uploaded_by", on_delete=models.CASCADE)
    liked_books = models.ManyToManyField(User, related_name="liked_by_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def user_validator(postData):
    errors = {}
    if views.validate_text(postData['fname']) == 0:
        errors["first_name_1"] = "First name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['fname']) == 1:
        errors["first_name_2"] = "First name should be at least 2 characters"
    if views.validate_text(postData['lname']) == 0:
        errors["last_name_1"] = "Last name should be letters not numbers! Sorry Elon Musk's baby!"
    if views.validate_text(postData['lname']) == 1:
        errors["last_name_2"] = "Last name should be at least 2 characters"
    if views.validate_text(postData['password'], min_length=8) == 1:
        errors["password"] = "Password should be at least 8 characters"
    if views.validate_email(postData['email']) == 2:
        errors["email_1"] = "Invalid email!"
    if views.validate_email(postData['email']) == 1:
        errors["email_2"] = "Email already exists!"
    if postData['password'] != postData['confirm']:
        errors["password"] = "Passwords do not match!"
    return errors


def book_validator(postData):
    errors = {}
    if views.validate_text(postData['desc'], min_length=5) == 1:
        errors['desc'] = "Description should be at least 5 characters"
    return errors


def insert_new_user(first_name, last_name, email, password, birthday):
    user = User.objects.create(
        first_name=first_name, last_name=last_name, email=email, password=password, birthday=birthday)
    return user


def is_duplicate_email(email):
    users = User.objects.filter(email=email).values()
    if len(users):
        return True
    return False


def get_user(email):
    users = User.objects.filter(email=email)
    if not len(users):
        return None
    return users[0]


def get_user_by_id(id):
    user = User.objects.get(id=id)
    return user


def insert_new_book(title, desc, id):
    book = Book.objects.create(
        title=title, desc=desc, books_uploaded=(User.objects.get(id=id)))
    return book


def get_book(id):
    book = Book.objects.get(id=id)
    return book


def all_books():
    all_books = Book.objects.all()
    return all_books


def edit_book(id, postData):
    book = Book.objects.get(id=id)
    book.title = postData['title']
    book.desc = postData['desc']
    book.save()


def add_to_favorites(book_id, user_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)
    liked_book = book.liked_books.add(user)
    return liked_book


def remove_from_favorites(book_id, user_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)
    removed_book = book.liked_books.remove(user)
    return removed_book
