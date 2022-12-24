from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.

def first(request):
    # calculation
    # fetch data from the Database
    return HttpResponse("<h1>this is the first Book</h1>")


def home(request):
    colors = ['Red', "Green", "Blue"]
    return render(request, "home.html", {"name": "Abraham", "age": 20, "colors": colors})

# user → API → urls → view → Response
# the View is a function that takes a 'request' and return a 'Response'
# template
# reder function → takes (request, html_template) ,  and returns HttpResponse

## Create a new App
#  1- run → python manage.py startapp <app_name>
#  2- register the new app in the 'INSTALLED_APPS'
#  3- create 'urls.py' module
#  4- create our 'view' functions
#  5- link route to the view
#  6- create a 'template' html file




def all(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books_list.html', {'books': books})



def get(request, id):
    try:
        book = Book.objects.get(id=id)
        # book = get_object_or_404(Book, id)
        return render(request, 'book.html', {'book': book})
    except:
        return HttpResponse("Does Not Exists")