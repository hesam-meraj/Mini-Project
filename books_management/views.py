from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import * 
from django.contrib import messages
from django.db.models import Q, Value
from django.db.models.functions import Concat



def homepage(request):
    search_query = request.GET.get('q', '')  
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    start_date = request.GET.get('start_date', '')
    books = Book.objects.all()
    if search_query:
        books = Book.objects.filter(
            Q(name__icontains=search_query) |
            Q(author__name__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    if min_price:
        books = books.filter(price__gte=min_price)
    if max_price:
        books = books.filter(price__lte=max_price)

    if start_date:
        books = books.filter(published_at__gte=start_date)

    context = {

    'books': books,
    'search_query': search_query,
    'min_price': min_price,
    'max_price': max_price,
    'start_date': start_date,

        
    }

    return render(request, 'homepage.html', context)




def add_category(request):
    if request.method == "POST":
        add_category_form = AddCategoryForm(request.POST)
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect("add_author")
    add_category_form = AddCategoryForm()
    
    return render(request, 'add_category.html', context={"add_category_form": add_category_form})

def add_author(request):
    if request.method == "POST":
        add_author_form = AddAuthorForm(request.POST)

        if add_author_form.is_valid():
            add_author_form.save()
            return redirect("add_book")
    add_author_form = AddAuthorForm()
    return render(request, 'add_author.html',context={"add_author_form": add_author_form})
    

def add_book(request):
    if request.method == "POST":
        add_book_form = AddBooksForm(request.POST)
        if  add_book_form.is_valid():
            add_book_form.save()
            msg = f'کتاب {add_book_form.cleaned_data["name"]} اضافه شد.'
            messages.success(request, msg)
            return redirect("homepage")
    else:
    
        add_book_form = AddBooksForm()
        
        return render(request,"add_book.html",context={"add_book_form": add_book_form})
    
def delete_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('homepage')
    return render(request, 'hompage.html')



def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        edit_book_form = AddBooksForm(request.POST, instance=book)
        if edit_book_form.is_valid():
            edit_book_form.save()
            return redirect('homepage')
    else:
        edit_book_form = AddBooksForm(instance=book)

    return render(request,"edit_book.html",context={"edit_book_form": edit_book_form, 'book': book})


