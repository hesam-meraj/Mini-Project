from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),

    path('',views.homepage, name="homepage"),
    path('add_category/',views.add_category, name="add_category"),
    path('add_author/',views.add_author, name="add_author"),
    path('add_book/',views.add_book, name="add_book"),

    path('about/',views.homepage, name="about"),
]