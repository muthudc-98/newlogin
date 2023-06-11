from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from application.forms import Signupform
from django.http import HttpResponseRedirect


def home(request):
	return render(request, 'apps/home.html')

@login_required
def result(request):
	return render(request, 'apps/result.html')

def signup(request):
	form=Signupform()
	if request.method=='POST':
		form=Signupform(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')

	return render(request ,'apps/signup.html',{'form':form})


