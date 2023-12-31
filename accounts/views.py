from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def registration_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')

    context={'form':form}
    return render(request, "accounts/regist.html", context)


def login_view(request):
    print("lll")
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
       # print(username,    password)
        user= authenticate(request, username=username, password=password)
        if user==None:
            context={"error": "Invalid Username or password"}
            return render(request,"accounts/login.html",context)
        print(user)
        login(request, user)
        return redirect('/')
    return render(request,"accounts/login.html",{})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login/")
    return render(request,"accounts/logout.html",{})

def register_view(request):

    return render(request, "accounts/regist.html", {})
