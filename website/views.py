from django.shortcuts import render, redirect, HttpResponse
from .models import Members
from django.contrib import messages

import datetime

def index(request):
    return render(request, 'landing.html', {'year': datetime.datetime.now().year})

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')

        try:
            user = Members.objects.get(email=email, passwd=passwd)
            request.session['user_email'] = user.email
            request.session['user_name'] = user.uname
            return redirect('convert_index')  # Make sure this matches converter.urls
        except Members.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('index')



def signup_view(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        passwd = request.POST['passwd']
        age = request.POST['age']

        if Members.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        Members.objects.create(uname=uname, email=email, passwd=passwd, age=age)
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'signup.html')
