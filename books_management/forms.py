from django import forms
from .models import *


class AddForm(forms.Form):
      name = forms.CharField(max_length=100)
      email = forms.CharField(max_length=255)
      bodye = forms.CharField(widget=forms.Textarea)

class AddCategoryForm(forms.ModelForm):
      
      
      class Meta:
            model = Category
            fields = ('name',)      

class AddBooksForm(forms.ModelForm):
      

      class Meta:
            model = Book
            fields = ('name', 'description','published_at', 'number_of_pages')
            labels = {'name': 'Enter the book name', 'description': 'Enter description for the book ','published_at':'Enter year-month-day for the day it is published', 'number_of_pages' : "Eneter the page numbers"}
            
class AddAuthorForm(forms.ModelForm):
      
      class Meta:
            model = Author
            fields = ('name', 'birth_date' ,'gender')