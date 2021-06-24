from django.urls import include, path

from .views import (ArticleAPIView, CreateBlogSubscribersView, CreateBlogView,
                    GetBlogView, UserCreateView)

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('blog-subscribe/', CreateBlogSubscribersView.as_view()),
    path('blog/', CreateBlogView.as_view()),
    path('blog/<int:pk>/', GetBlogView.as_view()),
    path('article/<str:pk>/', ArticleAPIView.as_view()),
]
