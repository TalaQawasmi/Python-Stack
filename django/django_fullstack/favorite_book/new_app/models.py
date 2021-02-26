from django.db import models
import re
import bcrypt

class UserManager(models.Model):
    def register_validator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name']="first name must be at least 2 characters"
        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "last name must be at least 2 characters"
        if len(postData['pw']) < 8:
            errors['pw'] = "password must be at least 8 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def registration(new_user):
    hash_pw = bcrypt.hashpw(new_user['pw'].encode(), bcrypt.gensalt()).decode()
    users = Users.objects.create(first_name=new_user['first_name'],last_name =new_user['last_name'],email=new_user['email'] ,password=hash_pw)
    return users.id
# Create your models here.
