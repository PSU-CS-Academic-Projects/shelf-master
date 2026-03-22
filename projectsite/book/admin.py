from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Borrowing

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth")
    search_fields = ("last_name", "first_name")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "publication_year", "available_copies")
    search_fields = ("title", "isbn")
    list_filter = ("genres", "publication_year")

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Updated to use the actual fields from your models.py
    list_display = ("book", "inventory_number", "condition", "is_available", "added_date")
    list_filter = ("condition", "is_available")

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("borrower", "book_instance", "borrow_date", "due_date", "is_returned")
    list_filter = ("is_returned", "due_date")
    search_fields = ("borrower__username", "book_instance__book__title")
    
# Register Genre normally since it has no custom admin class yet
admin.site.register(Genre)