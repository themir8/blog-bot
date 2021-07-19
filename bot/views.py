from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import UpdateAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Article, Blog, BlogSubscribers
from bot.models import BotUser
from . import serializers


class UserCreateView(APIView):

    def get(self, request):
        serializer = serializers.UserCreateSerializer()
        return Response(serializer.data)

    def post(self, request):
        try:
            user = serializers.UserCreateSerializer(data=request.data)
            if BotUser.objects.filter(user_id=request.data["user_id"]).exists():
                return Response(status=status.HTTP_200_OK)
            elif not BotUser.objects.filter(user_id=request.data["user_id"]).exists() and user.is_valid():
                user.save()
                return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserGetAPIView(UpdateAPIView):
    serializer_class = serializers.UserGetSerializer

    def get_queryset(self):
        return BotUser.objects.all()

    def get(self, request, pk):
        user = BotUser.objects.get(user_id=pk)
        serializer = serializers.UserGetSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class GetBlogView(UpdateAPIView):
    serializer_class = serializers.BlogGetSerializer

    def get_queryset(self):
        return Blog.objects.all()

    def get(self, request, pk):
        try:
            blog = Blog.objects.filter(owner__user_id=pk)
            serializer = serializers.BlogGetSerializer(blog, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
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


class ArticleGetAPIView(GenericAPIView, UpdateModelMixin):

    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = serializers.ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ArticlesAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all().order_by("-posted_date")
        serializer = serializers.ArticleSerializer(articles, many=True)
        return Response(serializer.data)
