from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def login_sign(request):
    return render(request, 'login_sign.html', {})    

def ChoixPet(request):
    return render(request, 'ChoixPET.html', {}) 

def donate(request):
    return render(request, 'donate.html', {})

def profil(request):
    return render(request, 'profil.html', {})              