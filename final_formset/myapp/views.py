from django.shortcuts import render,redirect,get_object_or_404
from .models import Author,Book
from .forms import AuthorForm,BookForm,CreateBookFormset,UpdateBookFormset
import json
from django.http import JsonResponse

# Create your views here.

def create_author(request):
    Authors = Author.objects.all()
    
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('create-author')
    form = AuthorForm()
    return render(request, 'myapp/createauthor.html', {'form':form,'Authors':Authors})


def create_book(request,id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author = id).values('id','book_name')
    
    if request.method == 'POST':
        formset = CreateBookFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                form_instance = form.save(commit=False)
                form_instance.author = author
                form_instance.save()
    else:
        formset = CreateBookFormset()
    return render(request, 'myapp/createbook.html',{'formset':formset,'books':books, 'author':author})
      
        
def update_books(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        formset = UpdateBookFormset(request.POST, instance=author)
        if formset.is_valid():
            formset.save()
            return redirect('create-author')
    else:
        formset = UpdateBookFormset(instance=author)
    
    return render(request, 'myapp/update_books.html', {'formset': formset, 'author': author})


