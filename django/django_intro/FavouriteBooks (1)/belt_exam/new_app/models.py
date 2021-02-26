from django.db import models
import re
import bcrypt
from datetime import date, datetime

class UserManager(models.Manager):
    def register_validator(self, user_info):
        errors = {}
        new_user = User.objects.filter(email = user_info['email'])
#names
        if (user_info['first_name'].isalpha()) == False: #user_info['first_name'] is from the form of registration
            if len(user_info['first_name']) <2 :
                errors["firstname"] = "First Name should be more than 2 characters." #["first_name"] is a key for errors dictionary can be any word
        if (user_info['last_name'].isalpha()) == False:
            if len(user_info['last_name']) <2 :
                errors["lastname"] = "Last Name should be more than 2 characters."
#email  
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(user_info['email']): #checking if email matches the regex           
            errors['email'] = "Invalid email address!"
        if len(new_user):
            errors['email'] = "email already exist"
#password
        if len(user_info['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if user_info['password'] != user_info['password_confirm']:
            errors['password_confirm']= "Password Dosent Match!"
        return errors

    def login_validator(self, user_info):
        errors = {}
        all_user = User.objects.filter(email = user_info['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(user_info['email']):
            errors['email'] = "Wrong email address!"
        if not len(all_user):
            errors['email'] = "Email not registered! /Wrong Email"
        if len(user_info['password']) < 8:
            errors["password"] = "Password should be 8 characters minimum"
        if len(all_user) and not bcrypt.checkpw(user_info['password'].encode(), all_user[0].password.encode()):
            errors["password"] = "Wrong Password!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def add_new_user(newUser):
    user = User.objects.filter(email = newUser['email'])
    if len(user) == 0:
        if newUser['password_confirm'] == newUser['password']:
            password = newUser['password']  #hashing user password
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=newUser['first_name'],last_name=newUser['last_name'],email=newUser['email'],password=hashed)  #newUser['key name from form']
            new_user_info = User.objects.last() 
            return new_user_info
    return False

def user_login(login_info):
    user_exist = User.objects.filter(email=login_info['email'])
    if len(user_exist):
        password= login_info['password']
        if bcrypt.checkpw(password.encode(), user_exist[0].password.encode()):
            return user_exist[0]
    return False


