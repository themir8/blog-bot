from django.urls import include, path

from .views import (ArticleGetAPIView, ArticlesAPIView, CreateBlogSubscribersView, CreateBlogView,
                    GetBlogView, UserCreateView, UserGetAPIView)

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('users/<int:pk>/', UserGetAPIView.as_view()),
    path('blog-subscribe/', CreateBlogSubscribersView.as_view()),
    path('blog/', CreateBlogView.as_view()),
    path('blog/<int:pk>/', GetBlogView.as_view()),
    path('articles/', ArticlesAPIView.as_view()),
    path('articles/<str:pk>/', ArticleGetAPIView.as_view()),
]
