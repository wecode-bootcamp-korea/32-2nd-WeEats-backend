from django.urls import path,include

urlpatterns = [
    path('users',include('users.urls')),
    path('restaurants', include('restaurants.urls')),
    path('reservations', include('reservations.urls')),
    path('mypage',include('mypage.urls'))
]
