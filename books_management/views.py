from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import * 
from django.contrib import messages

def homepage(request):
    books = Book.objects.all()
    return render(request, 'homepage.html',{'books': books})



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