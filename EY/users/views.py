"""Users views"""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

def login_view(request):
    """Login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

def signup_view(request):
    """Sign up view"""

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']
        gender = request.POST['gender']
        identification = request.POST['identification']
        age = request.POST['age']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirnmation does not match'})
        
        if len(identification) <= 6:
            return render(request, 'users/signup.html', {'error': 'Identification number is not valid'})
        
        if int(age) >= 150:
            return render(request, 'users/signup.html', {'error': 'The age is not correct'})
        
        if gender == "":
            return render(request, 'users/signup.html', {'error': 'The gender selection is not correct'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['first_last_name']
        user.save()

        profile = Profile(user=user)
        profile.first_name = request.POST['first_name']
        profile.first_last_name = request.POST['first_last_name']
        profile.second_last_name = request.POST['second_last_name']
        profile.identification = identification
        profile.age = age
        profile.gender = gender
        profile.save()

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')

