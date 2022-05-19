from django.urls import path
from users.views import KakaoSignIn

urlpatterns = [
    path('/login',KakaoSignIn.as_view()),
]
