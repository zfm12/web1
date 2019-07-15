from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from syy_contacts.models import Person
from django.contrib.auth.decorators import login_required

@login_required	
def search(request):
	#return render(request,'syy_contacts/search.html')
	#Persons=Person.objects.all()
	#if request.user.username:
	if 'q' in request.GET :
		q = request.GET['q']
		if not q:
			error = True
			return render_to_response('syy_contacts/search.html',{'error': error})
		else:
			query_list = Person.objects.filter(name__contains=q)
			if not query_list:       #如果名字查询不到，即name=q查询不到，就用Landline=q
				query_list = Person.objects.filter(Landline__contains=q)
				if not query_list:
					query_list = Person.objects.filter(telephone__contains=q)
					if not query_list:
						return render(request,'syy_contacts/search_result.html')
					else:
						return render(request,'syy_contacts/search_result.html',{'query_list':query_list})
				else:
					return render(request,'syy_contacts/search_result.html',{'query_list':query_list})
			else:
				return render(request,'syy_contacts/search_result.html',{'query_list':query_list})	
	else:
		error = True
		return render(request,'syy_contacts/search.html', {'error': error})
	#else:
		#return render_to_response('users/login.html',{'error': error})
		
		
		
		
	
