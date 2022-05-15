from django.urls        import path
from restaurants.views import MainView

urlpatterns = [
    path('',MainView.as_view()),
]