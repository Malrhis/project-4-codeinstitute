from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.show_reviews, name='show_review_route'),
    path('create', reviews.views.create_reviews, name='create_review_route'),
]
