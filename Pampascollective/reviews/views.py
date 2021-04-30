# reviews views.py
from django.shortcuts import (render,
                              HttpResponse,
                              redirect,
                              reverse,
                              get_object_or_404)
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

# Create your views here.


def show_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/show-reviews.template.html', {
        'reviews': reviews
    })


def create_reviews(request):
    if request.method == 'POST':
        create_review_form = ReviewForm(request.POST)

        if create_review_form.is_valid():
            review_created = create_review_form.save(commit=False)
            review_created.owner = request.user
            review_created.save()
            messages.success(
                request, f"New review {create_review_form.cleaned_data['title']} has been created")
            return redirect(reverse(show_reviews))
        else:
            return render(request, 'reviews/create-reviews.template.html', {
                'form': create_review_form
            })
    else:        
        create_review_form = ReviewForm()
        return render(request, 'reviews/create-reviews.template.html', {
            'form': create_review_form
        })
