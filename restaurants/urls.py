from django.urls       import path
from restaurants.views import RestaurantView

urlpatterns = [
    path('/<int:category_id>',RestaurantView.as_view())
]
