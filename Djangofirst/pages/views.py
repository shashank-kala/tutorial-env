from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1> Test code </h1>")
	return render(request,'home.html',{})
def contact_view(request,*args,**kwargs):
	#return HttpResponse("<h1> This is contact </h1>")
    return render(request,'Contact.html',{})