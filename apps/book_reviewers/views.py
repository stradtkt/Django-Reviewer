# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'book_reviewers/index.html')

def all_books(request):
    if request.session.get('id') == None:
        return redirect('/')
    context = {
        "books": Book.objects.all(),
        "user": User.objects.get(id=request.session['id'])
        }
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
            return redirect('/all-books')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return redirect('/')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)
        user = User.objects.get(email=email)
        request.session['id'] = user.id
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def process_book(request):
    errors = Book.objects.validate_book(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add-book')
    else:
        title = request.POST['title']
        content = request.POST['content']
        Book.objects.create(title=title, content=content)
        return redirect('/all-books')

def book_review(request, id):
    book = Book.objects.get(id=id)
    review = Review.objects.filter(book=book).order_by("-created_at")
    context = {"book": book, "reviews": review}
    return render(request, 'book_reviewers/review.html', context)



def process_review(request, id):
    errors = Review.objects.validate_review(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        title = request.POST['title']
        body = request.POST['body']
        user = User.objects.get(id=request.session['id'])
        book = Book.objects.get(id=id)
        Review.objects.create(title=title, body=body, user=user, book=book)
        return redirect('/')

def delete_review(request, book_id, review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    messages.success(request, "Deleted Review")
    return redirect('/{}/book-reviews'.format(book_id))