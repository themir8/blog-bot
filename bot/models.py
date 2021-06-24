import uuid

from django.contrib.auth import get_user_model
from django.db import models as db
from django.utils import timezone

from users.models import BotUser


class Category(db.Model):
    name = db.CharField("Category name", max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Blog(db.Model):
    id = db.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = db.CharField("Blog name", max_length=100)
    owner = db.ForeignKey(BotUser, verbose_name="Blog owner", related_name="botusers",
                          on_delete=db.CASCADE)
    category = db.ManyToManyField(
        Category, verbose_name="Blog's category", related_name="categories", max_length=3)

    def __str__(self) -> str:
        return self.name

    @property
    def blogsubscribers(self):
        return self.blogsubscribers_set.filter(blog__id=self.id)

    @property
    def articles(self):
        return self.article_set.filter(blog__id=self.id)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Article(db.Model):
    id = db.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = db.CharField("Article title", max_length=80)
    text = db.TextField("Article body")
    category = db.ForeignKey(
        Category, verbose_name="Category", on_delete=db.SET_NULL, null=True)
    author = db.ForeignKey(
        BotUser, verbose_name="Author", on_delete=db.SET_NULL, null=True
    )
    blog = db.ForeignKey(
        Blog, verbose_name="Blog", on_delete=db.SET_NULL, null=True
    )
    posted_date = db.DateTimeField("Posted date", default=timezone.now)
    edited_date = db.DateTimeField("Edited date", default=timezone.now)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class BlogSubscribers(db.Model):
    subscriber = db.OneToOneField(BotUser, verbose_name="Blog subscriber", related_name="blogsubscribers",
                                  on_delete=db.CASCADE, null=True, unique=True)
    blog = db.ForeignKey(Blog, verbose_name="Blog",
                         on_delete=db.CASCADE, null=True)

    def __str__(self) -> str:
        return self.blog.name

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Blog subscribers"


class ArticleView(db.Model):
    article = db.ForeignKey(
        Article, verbose_name="Article", on_delete=db.CASCADE)
    views = db.IntegerField("Article views", default=0)

    def __int__(self) -> int:
        return self.views
