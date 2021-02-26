from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def results(request):
    context = {
        "name": request.POST['Your Name'],
        "location" : request.POST['Dojo Location'],
        "favorite language" : request.POST['Favorite Language'],
        "comment" : request.POST['comment']
    }
    return render(request,"results.html",context)



# Create your views here.
