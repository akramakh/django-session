from django.db import models

# Create your models here.




class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name



class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None) # author_id
    name = models.CharField(max_length=255) # name, title, email, 
    num_of_pages = models.IntegerField(default=1)
    content = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.name

# 1 Create The Model
# 2 Create Migration for that model
    # python manage.py makemigrations
# 3 Reflect migration to the database 
    # python manage.py migrate

# table name = app name + _ + model name


# Opetations on Models CRUD
# Create:
# author1 = Author.objects.create (
#     name = "Ahmad",
#     bio = ""
# ) # → id = 1
# book1 = Book.objects.create(
#     author_id = 2,
#     # author = author1,
#     name = "Book #3",
#     num_of_pages = 10,
#     content = "Content of the Book #3 "
# )

# book2 = Book()
# book2.name = "Book #3"
# book2.num_of_pages = 30
# book2.author = 1
# book2.content = ""
# book2.save() # to save changes in the database

# # List → return multiple objects
# books = Book.objects.all() # list all objects
# Book.objects.count() # Count all objects

# # Retrieve (Get) → return single object
# Book.objects.all()[0] # return the first object
# Book.objects.all().first() # return the first object
# Book.objects.all().last() # return the last object
# Book.objects.get(id=2) # return the spicified object, else throw Exception
# Book.objects.get(name="Book #1") # return the spicified object, else throw Exception


# Update an object
# book = Book.objects.get(id=2)
# book.num_of_pages = 20
# book.content = book.content + " new."
# book.save() # to save changes in the database

# # Delete an object
# book = Book.objects.get(id=3)
# book.delete()




# Filter → return multiple objects
# Book.objects.filter()

# > → __gt → Eg.: Book.objects.filter(num_of_pages__gt=10)
# < → __lt → Eg.: Book.objects.filter(num_of_pages__lt=10)
# >= → __gte → Eg.: Book.objects.filter(num_of_pages__gte=10)
# <= → __lte → Eg.: Book.objects.filter(num_of_pages__lte=10)

# check if string contains: 
#   __contains: search with case-sinsitive → Book.objects.filter(name__contains="Book")
#   __icontains: search without case-sinsitive → Book.objects.filter(name__icontains="book")

# check is is null
# __isnull → Book.objects.filter(name__isnull=True)


# Order 
# Book.objects.all().order_by('created_at') → ASC order
# Book.objects.all().order_by('-created_at') → DESC order