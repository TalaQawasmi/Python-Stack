from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] =random.randint(1,100)
    return render(request,'index.html')
def game (request):
    if int(request.POST['guess']) == request.session['number']:
        request.session['result'] = 'correct'
    elif int(request.POST['guess']) > request.session['number']:
        request.session['result'] = 'high'
    else:
        request.session['result'] = 'low'
    return redirect('/')
def restart(request):
    del request.session['number']
    del request.session['result']
    return redirect('/')
