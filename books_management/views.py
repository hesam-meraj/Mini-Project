from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

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



def add_book(request):
    context = {
        'category_form': AddCategoryForm(),
        'book_form': AddBooksForm(),
        'author_form': AddAuthorForm(),
    }


    return render(request, 'form.html',context)






def about(request):
    return render(request,'about.html')