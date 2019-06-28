from django.shortcuts import render,redirect
from . import sql_work
# Create your views here.
def index(request):

    return render(request,'index.html')

def showSignUp(request):
    return render(request, 'signup.html')

def showSignIn(request):
    return render(request, 'signin.html')

def SignIn(request):
    name = request.GET['inputName']
    password = request.GET['inputPassword']

    if sql_work.check_user_password(name,password) !=[] :
        return render(request, 'shop.html')
    else:
        return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')
def SignUp(request):
    name = request.GET['inputName']
    email = request.GET['inputEmail']
    password = request.GET['inputPassword']
    if sql_work.check_user(name) ==[]:
        sql_work.add_user(name,email,password)
    return render(request, 'index.html')