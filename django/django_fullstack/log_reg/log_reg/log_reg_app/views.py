from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
import bcrypt

def main(request):
    return render(request,"index.html")

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user_id = models.registration(request.POST)
        messages.success(request, "user successfully Registered or Logged in")
        return redirect(f"success/{user_id}")

def registration(new_user):
    hash_pw = bcrypt.hashpw(new_user['pw'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=new_user['first_name'], last_name=new_user['last_name'], email=new_user['email'], password=hash_pw)
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


def success(user_id):
    context = {'this_user':User.objects.get(id=user_id)}
    return context


