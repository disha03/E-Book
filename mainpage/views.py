from django.shortcuts import render


def welcome(request):
	return render(request,'mainpage/welcome.html')


def books(request):
	return render(request, 'mainpage/books.html')
