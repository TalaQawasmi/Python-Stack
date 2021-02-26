from __future__ import unicode_literals
from django.db import models
import bcrypt, re
NAMEREG = re.compile(r'^[a-zA-Z.-]+( [a-zA-Z.-]+)*$')

class userDBManager(models.Manager):
    def check_create(self, data):
        errors = []
        if len(data['name']) < 3:
            errors.append(['name', "Name must be at least three characters in length."])
        if len(data['username']) < 3:
            errors.append(['name', "Username must be at least three characters in length."])
        if not re.match(NAMEREG, data['name']) or not re.match(NAMEREG, data['username']):
            errors.append(['name', 'Name and username must only include letters and "-" or "." please.'])
        if len(data['password']) < 8:
            errors.append(['password', 'Password must be at least 8 characters.'])
        if len(data['password_confirmation']) < 8 or data['password_confirmation'] != data['password']:
            errors.append(['password_confirmation', 'Password confirmation must be entered and match password.'])
        if errors:
            return [False, errors]
        else:
            user_check = userDB.objects.filter(username=data['username'])
            if user_check:
                errors.append(['user_check', 'Unable to register, please use alternate information.'])
                return [False, errors]
            newUser = userDB(name=data['name'], username=data['username'])
            newUser.save()
            return [True, newUser]

    def check_login(self, data):
        errors = []
        if len(data['username']) < 3:
            errors.append(['name', "Username must be at least three characters in length."])
        if len(data['password']) < 8:
            errors.append(['password', 'Password must be at least 8 characters.'])
        if errors:
            return [False, errors]
        else:
            check_user = userDB.objects.filter(username=data['username'])
            if not check_user:
                errors.append(['login', "Username or password not correct.  Please try again."])
            if errors:
                return [False, errors]
            else:
                user = check_user[0]
                return [True, user]




class userDB(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'ID: %s | Name: %s | Username %s' % (self.id, self.name, self.username)
    objects = userDBManager()