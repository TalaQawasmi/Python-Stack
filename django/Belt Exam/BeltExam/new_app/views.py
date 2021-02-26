from django.shortcuts import render, redirect 
from .models import *
from django.contrib import messages 
import bcrypt
from .models import Trip
def main(request):
    return render(request,"logAndreg.html")

def register(request):
    if request.POST:
        result = User.objects.register_validator(request.POST)
        #print(request.POST)
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return render(request,"logAndreg.html")
        else:
            #result = User.objects.validate_registration(request.POST)
            
            pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
            
            user=User.objects.create(Name=request.POST["Name"],password=pw_hash)
            request.session["logged_Name"] = request.POST["Name"]
            request.session["Reg"] = "Register"

            return redirect(success)

def login(request):
    if request.POST:
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return render(request, "index.html")

        else:
            try :
                user=User.objects.get(Name =request.POST["logged_Name"])

                if bcrypt.checkpw(request.POST['logged_pwd'].encode(), user.password.encode()):
                    request.session["logged_Name"] = request.POST["logged_Name"]
                    if "Reg" in request.session:
                        del request.session["Reg"]
                    return redirect(success)

                else:
                    return redirect(main)

            except:
                return redirect(main)

        return redirect(main)


def logout(request):
    if "logged_Name" in request.session:
        del request.session["logged_Name"]
    return redirect(main)

def success(request):
    
    if "logged_Name" not in request.session:
        return redirect(main)
    else:
        if "Reg" in request.session:
            status = "registered"
    
        else:
            status = "logged in"

        context = {
            "status": status,
            "user": User.objects.get(Name=request.session["logged_Name"]),
            #'user': User.objects.get(id = request.session['log']),
            'other_users': User.objects.all().exclude(id = request.session['logged_Name']),
        }

        return render(request, "success.html", context)
def index(request):
    # context = {
    #     'user': User.objects.get(id = request.session['user_id']),
    #     'other_users': User.objects.all().exclude(id = request.session['user_id']),
    # }
    return render(request, "addTrip.html")
# def add(request):
#     result = Trip.objects.validate_trip(request.POST, request.session['user_id'])

#     if type(result) == list:
#         for err in result:
#             messages.error(request, err)
#         return redirect('/add')
#     return render(request, 'addTrip.html')

# def add(request):
#     #return render(request, 'addTrip.html')
#     return redirect('/add')

def create(request):
    result = Trip.objects.validate_trip(request.POST, request.session['user_id'])
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/add')

    return redirect('/success')

def show(request, trip_id):
    context = {
        'trip': Trip.objects.get(id = trip_id)
    }
    return render(request, 'show.html', context)

def join(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    traveler = User.objects.get(id=request.session['user_id'])
    traveler.trips.add(trip)
    traveler.save()
    return redirect('/')




# Create your views here.
