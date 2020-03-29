from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account Created for {username} ')
			return redirect('login')
	else:		
		form=UserCreationForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		if u_form.is_valid():
			u_form.save()
			username=u_form.cleaned_data.get('username')
			messages.success(request,f'Account Info updated for {username}')
			return redirect('profile')


	else:
		u_form=UserUpdateForm(instance=request.user)

	return render(request,'users/profile.html',{'u_form':u_form})
			
