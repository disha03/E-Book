from django.shortcuts import render


def welcome(request):
	return render(request,'mainpage/welcome.html')


def books(request):
	return render(request, 'mainpage/books.html')

def contact(request):
	return render(request, 'mainpage/contact.html')

def about(request):
	return render(request, 'mainpage/about.html')