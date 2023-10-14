from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm,ProfileForm,ResetPasswordForm



def home(request):
    if request.user.is_authenticated:
        return render(request,"today/home.html")
    return redirect("signin")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been signed in!")
            return redirect("home")
        else:
            messages.success(request,"Invalid username or password!")

    return render(request,"today/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You have been signed out!")
    return redirect("signin")


def signup(request):
    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Account has been created.")
            return redirect("home")
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request,"today/signup.html",context)


def profile(request):
   
    crntuser=str(request.user) #for fix the bug even if not successful change username, it still will change to the updated one 
    if request.method == "POST":
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request,"You have edited you profile.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    context = {"form":form,"crntuser":crntuser}
    return render(request,"today/profile.html",context)

def resetPassword(request):
    if request.method == "POST":
  
        form = ResetPasswordForm(data=request.POST,user=request.user)
        if form.is_valid():
           
            form.save()
            messages.success(request,"You have reset your password.")
        
            update_session_auth_hash(request,form.user)
         
            return redirect("profile")
    else:
        form = ResetPasswordForm(user=request.user)
    context = {'form':form}
    return render(request,"today/resetPassword.html",context)