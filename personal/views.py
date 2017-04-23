from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request,'personal/basic.html', {'cont': ['if you would like to contact me, please email me','ael@email.com']})