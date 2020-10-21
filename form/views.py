from django.shortcuts import render, redirect
from .models import Feedback as Feed
 
from .forms import FeedbackForm, CreateUserForm
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group



@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='Employees')
			user.groups.add(group)
			messages.success(request, 'Account was created for' + username)
			return redirect('form:login')

	context = {'form':form}
	return render(request, 'form/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('form:home')
		else:
			messages.info(request,'Username or Password is incorrect')

	context = {}
	return render(request, 'form/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('form:login')

@login_required(login_url='form:login') 
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'form/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'form/home.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager'])
def feedbacks(request):
	feedbacks = Feed.objects.all()
	return render(request,'form/feedbacks.html', {'feedbacks':feedbacks})