
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..logapp.models import userDB
from .models import Trip

def main(request):
    return render(request, 'travel/main.html')

def dashboard(request):
    user = userDB.objects.get(id=request.session['user']['id'])
    context = {
        'trips': Trip.objects.filter(travelers=user),
        'other_trips': Trip.objects.all().exclude(travelers=user)
    }
    return render(request, 'travel/dashboard.html', context)


def join(request, id):
    user = userDB.objects.get(id=request.session['user']['id'])
    trip = Trip.objects.get(id=id)
    trip.travelers.add(user)
    trip.save()
    return redirect('travelapp:dashboard')

def destination(request, id):
    context = {
        'trip': Trip.objects.get(id=id),
        'travelers': userDB.objects.filter(trip_travelers__id=id)
    }
    return render(request, 'travel/destination.html', context)


def add_page(request):
    return render(request, 'travel/add.html')


def add(request):
    if request.method == "POST":
        user = userDB.objects.get(id=request.session['user']['id'])
        response = Trip.objects.check_trip(request.POST, user)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('travelapp:add_page')
    return redirect('travelapp:dashboard')


