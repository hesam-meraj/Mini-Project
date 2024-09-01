from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homepage),
    path('home/add/',views.add_book),
    path('home/show/',views.homepage),
    path('home/search/',views.homepage),
    path('home/edit/',views.homepage),
    path('home/delete/',views.homepage),
    path('home/filter/',views.homepage),
    path('about/',views.about),
    path('',views.test)
]