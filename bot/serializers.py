from rest_framework import serializers

from bot.models import Article, Blog, BlogSubscribers
from users.models import BotUser


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ['user_id', 'username', 'first_name', 'last_name',
                  'phone']


# end

# class GroupArticlesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['name', 'description', 'author', 'articles', 'private', 'slug', 'created_date']
