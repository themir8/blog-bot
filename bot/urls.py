from django.urls import path, include

from .views import UserCreateView


urlpatterns = [
    path('user/', UserCreateView.as_view()),
]
