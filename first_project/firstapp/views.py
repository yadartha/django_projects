from django.shortcuts import render

# Create your views here.
def index(request):
    name= 'yadartha'
    return render(request, "index.html", {'name': name})

def about(request):
    return render(request, "about.html")

def welcome(request):
    name='Edubridge'
    return render(request, "welcome.html", {'name': name})
