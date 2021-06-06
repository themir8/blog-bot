import uuid

from django.contrib.auth import get_user_model
from django.db import models as db
from django.utils import timezone

User = get_user_model()


class Category(db.Model):
    name = db.CharField("Category name", max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(db.Model):
    title = db.CharField("Article title", max_length=80)
    text = db.TextField("Article body")
    category = db.ForeignKey(
        Category, verbose_name="Category", on_delete=db.CASCADE)
    author = db.ForeignKey(
        User, verbose_name="Author", on_delete=db.CASCADE
    )
    posted_date = db.DateTimeField("Posted date", default=timezone.now)
    edited_date = db.DateTimeField("Edited date", default=timezone.now)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Blog(db.Model):
    id = db.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = db.CharField("Blog name", max_length=100)
    owner = db.ForeignKey(User, verbose_name="Blog owner",
                          on_delete=db.CASCADE)
    articles = db.ManyToManyField(
        Article, verbose_name="Articles in the blog")
    category = db.ManyToManyField(
        Category, verbose_name="Blog's category", max_length=3)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class BlogSubscribers(db.Model):
    subscriber = db.ForeignKey(User, verbose_name="Blog subscriber",
                               on_delete=db.CASCADE, null=True)
    blog = db.ForeignKey(Blog, verbose_name="Blog",
                         on_delete=db.CASCADE, null=True)

    def __str__(self) -> str:
        return self.blog.name

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Blog subscribers"
