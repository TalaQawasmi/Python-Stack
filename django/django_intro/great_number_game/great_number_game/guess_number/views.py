from django.shortcuts import render, redirect, HttpResponse
import random

def root(request):
    if 'random' not in request.session: 
        request.session['computer_random'] = random.randint(1, 100)
    return render(request, 'guess_the_number.html')

def guess(request):
    if request.method == "POST": 
        request.session['guessed_number'] = request.POST['numguess']
    if int(request.session['guessed_number']) > request.session['computer_random']:
        request.session['random']='high'
    elif int(request.session['guessed_number']) < request.session['computer_random']:
        request.session['random']='low'
    elif int(request.session['guessed_number']) == request.session['computer_random']:
        request.session['random']='true'
    return render(request,"guess_the_number.html")


def replay(request):
    del request.session['random']
    del request.session['computer_random']
    return redirect('/')






#def guess(request):

#request.session['numguess'] = request.POST['numguess']