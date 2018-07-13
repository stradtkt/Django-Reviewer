# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        # validate first and last name
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name needs to be two or more characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name needs to be two or more characters"
        # validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        # validate password
        if len(postData['password']) < 4:
            errors['password'] = "Please enter a longer password, needs to be four or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors
            
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def validate_book(self, postData):
        if len(postData['title']) < 2:
            errors['title'] = "The title needs to be two or more characters long"
        if len(postData['content']) < 10:
            errors['content'] = "The content for the book needs to be at least 10 characters long"

class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def validate_review(self, postData):
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters"
        if len(postData['body']) < 10:
            errors['body'] = "The body for the review needs to be at least 10 characters long"
            

class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    objects = ReviewManager()