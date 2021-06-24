from rest_framework import serializers

from bot.models import Article, Blog, BlogSubscribers
from users.models import BotUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ['user_id', 'username', 'first_name', 'last_name',
                  'phone']


class ArticleGetSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True)
    blog = serializers.SlugRelatedField(
        slug_field="name", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class BlogSubscribersGetSerializer(serializers.ModelSerializer):

    subscriber = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    blog = serializers.SlugRelatedField(
        slug_field="name", read_only=True)

    class Meta:
        model = BlogSubscribers
        fields = "__all__"


class BlogSubscribersCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogSubscribers
        fields = "__all__"


class BlogGetSerializer(serializers.ModelSerializer):

    owner = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True)
    blogsubscribers = BlogSubscribersGetSerializer(
        source='blogsubscribers_set', many=True, read_only=True)
    articles = ArticleGetSerializer(
        source='article_set', many=True, read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = "__all__"

# end

# class GroupArticlesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['name', 'description', 'author', 'articles', 'private', 'slug', 'created_date']
