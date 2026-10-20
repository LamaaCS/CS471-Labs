
from django.urls import path
from . import views

urlpatterns = [
    # Lab 3 and Lab 4
    path('', views.index, name='books.index'),
    path('index2/<int:val1>/', views.index2),
    path('list_books/', views.list_books, name='books.list_books'),
    path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
    path('aboutus/', views.aboutus, name='books.aboutus'),

    # Lab 5 - Task 1
    path('html5/links', views.html5_links, name='books.html5_links'),

    # Lab 5 - Task 2
    path('html5/text/formatting', views.html5_formatting, name='books.html5_formatting'),

    # Lab 5 - Task 3
    path('html5/listing', views.html5_listing, name='books.html5_listing'),

    # Lab 5 - Task 4
    path('html5/tables', views.html5_tables, name='books.html5_tables'),
]
