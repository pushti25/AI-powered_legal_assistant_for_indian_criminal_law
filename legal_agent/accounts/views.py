from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# ---------------- SIGNUP ----------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
