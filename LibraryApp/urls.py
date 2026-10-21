from django.urls import path
from LibraryApp import views


urlpatterns=[
    path('books/', views.BookListCreateView.as_view()),
    path('book/<int:pk>/', views.BookRetrieveUpdateDeleteView.as_view()),
    path('book/<int:pk>/issue/', views.IssueBookView.as_view()),
    path('book/<int:pk>/return/', views.ReturnBookView.as_view()),
]