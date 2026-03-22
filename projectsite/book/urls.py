from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('member-history/<str:username>/', views.member_history, name='member-history'),
]