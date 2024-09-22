from django import forms
from .models import *

class AddCategoryForm(forms.ModelForm):
      
      
      class Meta:
            model = Category
            fields = ('name',)      

class AddBooksForm(forms.ModelForm):
      

      class Meta:
            model = Book
            fields = '__all__'
            labels = {'name': 'Enter the book name', 'description': 'Enter description for the book ','published_at':'Enter year-month-day for the day it is published', 'number_of_pages' : "Eneter the page numbers"}
            
class AddAuthorForm(forms.ModelForm):
      
      class Meta:
            model = Author
            fields = '__all__'