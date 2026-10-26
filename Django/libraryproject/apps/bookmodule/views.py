
from django.http import HttpResponse
from django.shortcuts import render


# Lab 3 + Lab 4: Home Page
def index(request):
    name = request.GET.get("name") or "Lama"
    return render(request, "bookmodule/index.html", {"name": name})


# Lab 3: URL Parameter
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


# Lab 4: List of Books
def list_books(request):
    return render(request, "bookmodule/list_books.html")


# Lab 4: About Us
def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


# Lab 3 + Lab 4: Book Details
def viewbook(request, bookId):
    book1 = {
        'id': 123,
        'title': 'Continuous Delivery',
        'author': 'J. Humble and D. Farley'
    }

    book2 = {
        'id': 456,
        'title': 'Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1

    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, "bookmodule/one_book.html", context)


# Lab 5 - Task 1: HTML5 Links
def html5_links(request):
    return render(request, "bookmodule/links.html")


# Lab 5 - Task 2: Text Formatting
def html5_formatting(request):
    return render(request, "bookmodule/formatting.html")


# Lab 5 - Task 3: Nested Lists
def html5_listing(request):
    return render(request, "bookmodule/listing.html")


# Lab 5 - Task 4: HTML Tables
def html5_tables(request):
    return render(request, "bookmodule/tables.html")


# Lab 6 - Task 2: Books List
def __getBooksList():
    book1 = {
        'id': 12344321,
        'title': 'Continuous Delivery',
        'author': 'J.Humble and D. Farley'
    }

    book2 = {
        'id': 56788765,
        'title': 'Reversing: Secrets of Reverse Engineering',
        'author': 'E. Eilam'
    }

    book3 = {
        'id': 43211234,
        'title': 'The Hundred-Page Machine Learning Book',
        'author': 'Andriy Burkov'
    }

    return [book1, book2, book3]


# Lab 6 - Task 2: Handle Search Form
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Filter books
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(
            request,
            'bookmodule/bookList.html',
            {'books': newBooks}
        )

    return render(request, 'bookmodule/search.html')
