from django.db import models as db
from django.contrib.auth.models import User
from django.utils import timezone


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
    category = db.ForeignKey(Category, verbose_name="Category", on_delete=db.CASCADE)
    author = db.ForeignKey(
        User, verbose_name="Author", on_delete=db.CASCADE
    )
    posted_date = db.DateTimeField("Posted date", default=timezone.now())
    edited_date = db.DateTimeField("Edited date", default=timezone.now())

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
