from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

def main(request):
    return render(request,"regi-login.html")

def success(request):
    if 'user_id' in request.session:
        context = {
            'first_name':request.session['first_name'],
            'last_name':request.session['last_name']
        }
        return render(request,'success.html',context)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        errors = models.User.objects.register_validator(request.POST) #check if there are errors in error dictionary and redirect to same page to fill form again 
        if len(errors)>0:  #if errors exist loop over the dictionary and show the messages
            for key, value in errors.items():
                messages.error(request, value) #show the messages value
            return redirect('/')                                                                   
        else: #if there are no errors >> create new user
            user = models.add_new_user(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                return redirect('/success')
    return redirect('/')

def login(request):
    if request.method=='POST':
        errors = models.User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = models.user_login(request.POST)
            if user is not None:
                if 'user_id' not in request.session:
                    request.session['user_id'] = user.id
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name
                    return redirect('/success')
    return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['first_name']
        del request.session['last_name']
    return redirect('/')