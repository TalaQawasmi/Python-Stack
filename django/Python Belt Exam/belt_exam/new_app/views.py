from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .models import *

def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def main(request):
    return render(request,"regi_login.html")

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
        errors = models.User.objects.register_validator(request.POST)  
        if len(errors)>0: 
            for key, value in errors.items():
                messages.error(request, value) 
            return redirect('/')                                                                   
        else: 
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

def quotes(request):
	user = current_user(request)

	context = {
		'user': user,
		'quotable_quotes': Quote.objects.exclude(favorites = user),
		'favorites': user.favorites.all()
	}

	return render(request, 'new_app/quotes.html', context)

def create(request):
	if request.method != 'POST':
		return redirect('/')
	##adds item to quotes
	check = Quote.objects.validateQuote(request.POST)
	if request.method != 'POST':
		return redirect('/quotes')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="add_item")
			return redirect('/quotes')
	if check[0] == True:

		quote = Quote.objects.create(
			content = request.POST.get('content'),
			poster = current_user(request),
			author = request.POST.get('author')
			)

		return redirect('/quotes')
	return redirect('/quotes')


def add_favorite(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.add(favorite)

	return redirect('/quotes')

def remove_favorite(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.remove(favorite)

	return redirect('/quotes')

def show_user(request, id):

	user =  User.objects.get(id = id)
	context = {
		'user': user,
		'favorites': user.favorites.all()		
	}
	return render(request, 'new_app/success.html', context)