from django.urls        import path
from restaurants.views import RestaurantView

urlpatterns = [
    path('',RestaurantView.as_view()),
]