from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
        return redirect("organizations")

    return render(request, "user/login.html")
