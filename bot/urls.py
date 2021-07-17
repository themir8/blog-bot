from django.urls import include, path

from .views import (ArticleGetAPIView, ArticlesAPIView, CreateBlogSubscribersView, CreateBlogView,
                    GetBlogView, UserCreateView)

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('blog-subscribe/', CreateBlogSubscribersView.as_view()),
    path('blog/', CreateBlogView.as_view()),
    path('blog/<int:pk>/', GetBlogView.as_view()),
    path('articles/', ArticlesAPIView.as_view()),
    path('articles/<str:pk>/', ArticleGetAPIView.as_view()),
]
