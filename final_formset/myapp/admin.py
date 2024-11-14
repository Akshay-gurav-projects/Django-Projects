from django.contrib import admin
from .models import Author,Book

# Register your models here.
admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=["author","book_name","pages"]