from django.urls import path
from .views import first, home, all, get

'first/'
""
urlpatterns = [
    path("first/", first),
    path("home/", home),
    path("<int:id>/", get),
    path("", all),
]


# book/ → home
# book/first → first