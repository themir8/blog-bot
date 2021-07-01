from rest_framework.fields import ImageField
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import UpdateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Article, Blog, BlogSubscribers
from users.models import BotUser
from . import serializers


class UserCreateView(APIView):

    def get(self, request):
        serializer = serializers.UserCreateSerializer()
        return Response(serializer.data)

    def post(self, request):
        try:
            user = serializers.UserCreateSerializer(data=request.data)
            if user.is_valid():
                user.save()
            return Response(status=201)
        except:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetBlogView(UpdateAPIView):
    serializer_class = serializers.BlogGetSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(owner__user_id=pk)
            serializer = serializers.BlogGetSerializer(blog)
            return Response(serializer.data)
        except:
            return Response({'status': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CreateBlogView(APIView):

    serializer_class = serializers.BlogCreateSerializer

    def get(self, request):
        serializer = serializers.BlogCreateSerializer()
        return Response(serializer.data)

    def post(self, request):
        blog = serializers.BlogCreateSerializer(data=request.data)
        owner = Blog.objects.get(owner__id=request.POST.get("owner"))
        if owner:
            data = {"detail": "У вас уже есть свой блог!"}
            return Response(data, status=404)
        else:
            if blog.is_valid():
                blog.save()
            return Response(status=201)


class CreateBlogSubscribersView(APIView):

    def post(self, request):
        blog = serializers.BlogSubscribersCreateSerializer(data=request.data)
        if blog.is_valid():
            blog.save()
        return Response(status=201)


class ArticleAPIView(GenericAPIView, UpdateModelMixin):

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleGetSerializer

    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = serializers.ArticleGetSerializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# class ArticleCreateView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         article = serializers.ArticleCreateSerializer(data=request.data)
#         if article.is_valid():
#             article.save()
#         return Response(status=201)


# class ArticleEditView(GenericAPIView, UpdateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = serializers.ArticleCreateSerializer
#     permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

#     def get(self, request, pk):
#         article = Article.objects.get(id=pk)
#         serializer = serializers.ArticleDetailSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


# # GroupArticles views
# class PublicGroupListView(APIView):
#     permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

#     def get(self, request):
#         groups = GroupArticles.objects.filter(private=False)
#         serializer = serializers.GroupArticleListSerializer(groups, many=True)
#         return Response(serializer.data)


# class GroupListView(APIView):
#     permission_classes = [IsAuthenticatedAndOwnerOrReadOnly]

#     def get(self, request):
#         groups = GroupArticles.objects.all()
#         serializer = serializers.GroupArticleListSerializer(groups, many=True)
#         return Response(serializer.data)


# class GroupDetailView(APIView):
#     def get(self, request, pk):
#         group = GroupArticles.objects.get(id=pk)
#         serializer = serializers.GroupArticleDetailSerializer(group)
#         return Response(serializer.data)
# # end
