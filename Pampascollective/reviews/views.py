# reviews views.py
from django.shortcuts import (render,
                              HttpResponse,
                              redirect,
                              reverse,
                              get_object_or_404)
from django.contrib import messages
from .models import Review

# Create your views here.


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/show-reviews.template.html',{
        'reviews':reviews
    })