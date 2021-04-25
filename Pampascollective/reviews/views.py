from django.shortcuts import render

# Create your views here.
def show_reviews(request):
    return render(request, 'reviews/show-reviews.template.html')