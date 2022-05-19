from django.urls       import path
from restaurants.views import RestaurantView, RestaurantDetailView

urlpatterns = [
    path('',RestaurantView.as_view()),
    path('/<int:restaurant_id>', RestaurantDetailView.as_view())
]