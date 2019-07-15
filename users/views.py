from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request): #注销用户
	logout(request)
	return HttpResponseRedirect(reverse('syy_topics:index'))

def register(request):   #注册新用户
	if request.method !='POST':
		form=UserCreationForm()
	else:
		form=UserCreationForm(data=request.POST)
		
		if form.is_valid():
			new_user=form.save()
			#用户自动登录，再重定向到主页
			
			authenticated_user=authenticate(username=new_user.username,
			password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('syy_topics:index'))
	context={'form':form}
	return render(request,'users/register.html',context)