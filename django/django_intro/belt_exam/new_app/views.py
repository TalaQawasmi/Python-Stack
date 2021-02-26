from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user_id = models.registration(request.POST)
        messages.success(request, "user successfully Registered or Logged in")
        return redirect(f"success/{user_id}")


def log_in(request):
    context = models.log_in(request.POST)
    if context['flag'] == True:
        messages.success(request, "user successfully Registered or Logged in")
        return redirect(f"success/{context['this_user'].id}")
    else:
        messages.error(request, "you need to register")
        return redirect("/")


def success(request, user_id):
    user = models.success(user_id)
    request.session['logged_id'] = user['this_user'].id
    return render(request,'success.html', user)
