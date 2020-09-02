from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.session.has_key('loggedin'):
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Loggedin")
            request.session['loggedin'] = True
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'register/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")
                return redirect('signup')

            elif len(username) < 2:
                messages.error(request, "Your Username is too Short")
                return redirect('signup')

            elif len(password1) < 8:
                messages.error(request, "Your Password is too Short")
                return redirect('signup')

            else:
                myuser = User.objects.create_user(username, email, password1)
                myuser.save()
                messages.success(request, "User Created")
        else:
            messages.error(request, "Password do not match")
            return redirect('signup')

        return redirect('login')
    else:
        return render(request, 'register/signup.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    messages.success(request, "Loggedout")
    return redirect('login')
