from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('book-table/', views.book_table, name='book_table'),
    path('signup/', views.signup, name='signup'),
    path('add-review/', views.add_review, name='add_review'),
] 