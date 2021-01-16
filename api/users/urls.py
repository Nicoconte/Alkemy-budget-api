from django.urls import path

from .views import UserRegister, UserAuth

urlpatterns = [
    path('users/', UserRegister.as_view()),
    path('users/auth/', UserAuth.as_view())
]
