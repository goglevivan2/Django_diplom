from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')

def showSignUp(request):
    return render(request, 'signup.html')

def showSignIn(request):
    return render(request, 'signin.html')

def SignIn(request):
    return render(request, 'index.html')