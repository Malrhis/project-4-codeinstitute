from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.show_reviews)
]
