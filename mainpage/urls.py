from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome,name="mainpage"),
    path('books/',views.books,name="books"),
    path('contact/',views.contact,name="contact")
]
