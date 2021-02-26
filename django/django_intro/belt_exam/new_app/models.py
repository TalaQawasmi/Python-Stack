from django.db import models
import re
import bcrypt
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first_name should be at least 4 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last_name should be at least 4 characters"
        if len(postData['pw']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['pw'] != postData['pw_cn']:
            errors["pw"] = "password should match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def registration(new_user):
    hash_pw = bcrypt.hashpw(new_user['pw'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=new_user['first_name'],last_name=new_user['last_name'],email=new_user['email'],password=hash_pw)
    return user.id


def log_in(log_in_data):
    user = User.objects.get(email=log_in_data['email'])
    if bcrypt.checkpw(log_in_data['pw'].encode(), user.password.encode()):
        context= {
            'flag': True,
            'this_user': user
        }
        return context
    else:
        context = {
            'flag': False
        }
        return context


def success(Nuser_id):
    context = {'this_user':User.objects.get(id=user_id)}
    return context


