from rest_framework import fields, serializers

from bot.models import Article, Blog, BlogSubscribers
from bot.models import BotUser


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"


class BlogSubscribersSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogSubscribers
        fields = "__all__"


class BlogGetSerializer(serializers.ModelSerializer):

    blogsubscribers = BlogSubscribersSerializer(
        source='blogsubscribers_set', many=True, read_only=True)
    # blogsubscribers = fields.IntegerField
    articles = ArticleSerializer(
        source='article_set', many=True, read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotUser
        fields = ['user_id', 'username', 'first_name',
                  'last_name']


class UserGetSerializer(serializers.ModelSerializer):

    follows = BlogSubscribersSerializer()
    blogs = BlogCreateSerializer(many=True)

    class Meta:
        model = BotUser
        fields = "__all__"
