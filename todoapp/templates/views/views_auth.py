from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Auth-related routes
def signup(request):
    if request.method == 'GET':
    	return render(request, 'todoapp/signup.html')

    elif request.method == 'POST':
    	# All variables coming from the request object
    	username = request.POST['username']
    	password = request.POST['password']
    	firstname = request.POST['firstname']
    	lastname = request.POST['lastname']

    	# importing variables into the database
    	try:
    		user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname)
    		# used to have the signup function automatically log in
    		if user is not None:
    			return login(request)
    	except:
    		return render(request, 'todoapp/signup.html', {'error': 'Username already exists'})


def login(request):
    if request.method == 'GET':
    	return render(request, 'todoapp/login.html')
    elif request.method == 'POST':
    	username = request.POST['username']
    	password = request.POST['password']
    	user = auth.authenticate(username=username, password=password)

    	if user is not None: 
    		auth.login(request, user)
    		return redirect('index')
    	else:
    		return render(request, 'todoapp/login.html', {'error': 'Invalid Credentials'})

def logout(request):
    auth.logout(request)
    return redirect('index')