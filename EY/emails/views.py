"""Emails views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime

# Exceptions
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt

# Models
from django.contrib.auth.models import User
from users.models import Profile
from emails.models import Emails

@login_required
def home(request):
    """List users."""
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
    
    profiles = Profile.objects.all()
    return render(request, 'emails/home.html', {'profiles': profiles})

@login_required
def add_user(request):
    """Add user."""
    return render(request, 'emails/add_user.html')

@login_required
def modify_user(request):
    """Modify user."""
    if request.method == "POST":
        user = User.objects.get(pk=request.POST['id_user'])
        profile_user = Profile.objects.get(user=user)
    
    return render(request, 'emails/modify_user.html', {'profile': profile_user})

@login_required
def modify_user_save(request):
    """Modify user save."""
    if request.method == "POST":
        
        if len(request.POST['identification']) <= 6:
            return render(request, 'emails/modify_user.html', {'error': 'Identification number is not valid'})
        
        if int(request.POST['age']) >= 150:
            return render(request, 'emails/modify_user.html', {'error': 'The age is not correct'})
        
        if request.POST['gender'] == "":
            return render(request, 'emails/modify_user.html', {'error': 'The gender selection is not correct'})
        
        user = User.objects.get(pk=request.POST['id_user'])
        profile_user = Profile.objects.get(user=user)
        user.username = request.POST['username']
        profile_user.first_name = request.POST['first_name']
        profile_user.first_last_name = request.POST['first_last_name']
        profile_user.second_last_name = request.POST['second_last_name']
        profile_user.identification = request.POST['identification']
        profile_user.age = request.POST['age']
        profile_user.gender = request.POST['gender']

        user.save()
        profile_user.save()
    
    profiles = Profile.objects.all()
    return render(request, 'emails/home.html', {'profiles': profiles})

@login_required
def remove_user(request):
    """List users."""
    if request.method == "POST":
        user = User.objects.get(pk=request.POST['id_user'])
        user.delete()
    profiles = Profile.objects.all()
    return render(request, 'emails/home.html', {'profiles': profiles})

@login_required
def emails_user(request):
    """Emails users."""
    profiles = Profile.objects.all()
    if request.method == "GET":
        user = User.objects.get(pk = request.GET.get('id'))
        emails = Emails.objects.filter(user = user).order_by('priority')
        return render(request, 'emails/home_email.html', {'id_user': request.GET.get('id'), 'emails': emails,'profiles': profiles})
    else:
        if request.method == "POST":
            user = User.objects.get(pk=request.POST['id_user'])
            email = Emails(user=user)
            email.email = request.POST['email']
            email.priority = request.POST['priority']
            try:
                email.save()
            except IntegrityError:
                return render(request, 'emails/emails_add.html', {'error': 'Email is already in use', 'id': request.POST['id_user']})

            emails = Emails.objects.filter(user = user).order_by('priority')
            return render(request, 'emails/home_email.html', {'id_user': request.POST['id_user'], 'emails': emails,'profiles': profiles})
        else:
            return render(request, 'emails/home.html', {'profiles': profiles})

@login_required
def emails_add(request):
    """Emails add."""
    if request.method == "POST":
        id_user = request.POST['id_user']
    return render(request, 'emails/emails_add.html', {'id': id_user})

@login_required
def emails_modify(request):
    """Emails modify."""
    if request.method == "POST":
        email_user = Emails.objects.get(pk = request.POST['id_email'])
    
    return render(request, 'emails/emails_modify.html', {'id': request.POST['id_email'], 'email': email_user})

@login_required
def emails_modify_save(request):
    """Emails modify save."""
    profiles = Profile.objects.all()
    if request.method == "POST":
        email = Emails.objects.get(pk = request.POST['id_email'])
        email.email = request.POST['email']
        email.priority = request.POST['priority']

        try:
            email.save()
        except IntegrityError:
            return render(request, 'emails/emails_add.html', {'error': 'Email is already in use', 'id': request.POST['id_email']})

    emails = Emails.objects.filter(user = email.user).order_by('priority')
    return render(request, 'emails/home_email.html', {'id_user': email.user.pk, 'emails': emails,'profiles': profiles})

@login_required
def emails_remove(request):
    """Emails remove."""
    profiles = Profile.objects.all()
    
    if request.method == "POST":
        email = Emails.objects.get(pk=request.POST['id_email'])
        email.delete()

        emails = Emails.objects.filter(user = email.user).order_by('priority')
    return render(request, 'emails/home_email.html', {'id_user': email.user.pk, 'emails': emails,'profiles': profiles})

@login_required
def filter_user(request):
    """List users."""
    profiles_emails = []

    if request.method == "POST":
        emails = Emails.objects.filter(email__contains=request.POST['filter_emails'])

        for email in emails:
            profiles_emails.append(email.user)
        
        profiles = Profile.objects.filter(user__in=profiles_emails)

    return render(request, 'emails/home.html', {'profiles': profiles})

