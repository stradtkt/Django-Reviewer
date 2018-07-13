# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'book_reviewers/index.html')

def all_books(request):
    context = {"books": Book.objects.all()}
    return render(request, 'book_reviewers/all-books.html', context)

def add_book(request):
    return render(request, 'book_reviewers/add-book.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if is_pass:
            request.session['id'] = user[0].id
            return redirect('all-books')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return redirect('/')

def process_book(request):
    title = request.POST['title']
    content = request.POST['content']
    valid = True
    if title == "":
        print("The title cannot be empty")
        valid = False
    if content == "":
        print("The content cannot be empty")
        valid = False
    if valid: 
        book = Book.objects.create(title=title, content=content)
    else:
        return redirect('add-book')

def book_review(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "reviews": Reviews.objects.get(id=id)
    }
    return render(request, 'book_reviewers/review.html', context)



def process_review(request):
    title = request.POST['title']
    body = request.POST['body']
    review = Review.objects.create(title=title, body=body)
    return redirect('/')
    