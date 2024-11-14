from django import forms
from .models import Author,Book
from django.forms import formset_factory,inlineformset_factory



class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name','pages']


# BookFormset = formset_factory(BookForm,extra=0,can_delete=False)
CreateBookFormset = inlineformset_factory(Author, Book, form=BookForm, extra=0, can_delete=False)
UpdateBookFormset = inlineformset_factory(Author, Book, form=BookForm, extra=0, can_delete=True)


