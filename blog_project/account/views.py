from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def signup(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        e=request.POST['email']
        user = User.objects.create_user(u,e,p)
        user.save()
        return HttpResponse("registered suessfully!")
    return render(request,'account/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("login sucessful!")
        else:
            return HttpResponse("wrong username and password")
    return render(request,'account/signin.html')

def logged_out(request):
    logout(request)
    return render(request,'account/logout.html')

def basic(request):

    return render(request,'account/base.html')
