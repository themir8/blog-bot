import os

import requests

from .models import Article, User, Blog


def create_user(user: User) -> int:
    r = requests.post(os.getenv("BASE_URL")+"/user/", data=user.dict())
    return r.status_code


def get_blog(user_id: int) -> Blog:
    r = requests.get(os.getenv("BASE_URL")+"/blog/"+str(user_id))
    blog = Blog(**r.json())
    return blog


def get_article(article_id: str) -> Article:
    r = requests.get(os.getenv("BASE_URL")+"/article/"+article_id)
    article = Article(**r.json())
    return article
