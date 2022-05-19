from django.urls import path

from mypage.views import MyPageView

urlpatterns = [
    path('',MyPageView.as_view()),
    path('/<int:reservation_id>',MyPageView.as_view())
]
