from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"index.html")
def register(request):
    if request.method=="POST":
        user_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['pswd']
        confirm_password=request.POST['pswd1']
        #to store the values in the database
        user=User.objects.create_user(username=user_name,email=email,password=confirm_password)
        user.save()
        return render(request,"login.html")
    else:
        return render(request,"register.html")
def login(request):
    if request.method=="POST":
        user_name=request.POST['username']
        password=request.POST['pswd']

        user=auth.authenticte(username=user_name,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.info(request,"You login successfully")
            return render(request,"blogs.html,contactus.html,reviewers.html,authors.html")
            
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def reviewers(request):
    return render(request,"reviewers.html")
def blogs(request):
    return render(request,"blogs.html")
def authors(request):
    return render(request,"authors.html")
def contactus(request):
    return render(request,"contactus.html")