from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def homepage(request): 
    return render(request,'home.html')


 
def test(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():


            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)






    form = AddForm()
    return render(request, 'form.html',{'form': form})

# name
# 'name', 'description','published_at', 'number_of_pages'
# name', 'birth_date' ,'gender'
def add_book(request):
    category_form =  AddCategoryForm()
    book_form =  AddBooksForm()
    author_form = AddAuthorForm()
    if request.method == 'POST':
        category_form =  AddCategoryForm(request.POST)
        book_form =  AddBooksForm(request.POST)
        author_form = AddAuthorForm(request.POST)
        if category_form.is_valid() and book_form.is_valid() and author_form.is_valid():
            category_name = category_form.cleaned_data['name']
            book_name = book_form.cleaned_data['name']
            book_des = book_form.cleaned_data['description']
            book_p = book_form.cleaned_data['published_at']
            np = book_form.cleaned_data['number_of_pages']
            au_name = author_form.cleaned_data['name']
            au_birth = author_form.cleaned_data['birth_date']
            au_gen = author_form.cleaned_data['gender']
            

            ob_cat = Category.objects.create(name=category_name)
            ob_book = Book(name=book_name,description=book_des,published_at=book_p,number_of_pages=np)
            ob_auth = Author(name=au_name,birth_date=au_birth,gender=au_gen)
            ob_cat.save()
            print('data stored1')
            ob_book.save()
            print('data stored2')

            ob_auth.save()
            print('data stored3')


    return render(request, 'form.html',{'category_form': AddCategoryForm(),'book_form': AddBooksForm(),'author_form': AddAuthorForm(),})






def about(request):
    return render(request,'about.html')