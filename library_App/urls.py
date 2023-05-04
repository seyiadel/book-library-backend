from django.urls import path
from library_App.views import SignUpUser, LogInUser, SingleBook, AllBooks, CreateBook, LibraryUser
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path("user/", LibraryUser.as_view(), name = 'user'),
    path("signup/", SignUpUser.as_view(), name ='signup'),
    path("login/",LogInUser.as_view(), name = 'login'),
    path("logout/", LogoutView.as_view(), name = 'logout'),
    path("logout-all/", LogoutAllView.as_view(), name ='logout-all'),
    path("book/",CreateBook.as_view(), name = 'add-book'),
    path("book/<int:pk>/", SingleBook.as_view(), name = 'get-book'),
    path("books/", AllBooks.as_view(), name = 'books'),
]