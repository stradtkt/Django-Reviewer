from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^all-books$', views.all_books),
    url(r'^(?P<id>\d+)/book-reviews$', views.book_review),
    url(r'^book-reviews/(?P<id>\d+)/process_review$', views.process_review),
    url(r'^book-reviews/(?P<book_id>\d+)/delete/(?P<review_id>\d+)$', views.delete_review),
    url(r'^add-book$', views.add_book),
    url(r'^process_book$', views.process_book)
]