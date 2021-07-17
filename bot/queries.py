import os
import dotenv

import requests

from .models import Article, User, Blog


dotenv.load_dotenv()
BASE_URL = str(os.getenv("BASE_URL"))


def create_user(user: User) -> int:
    r = requests.post(BASE_URL+"/user/", data=user.dict())
    return r.status_code


def get_blog(user_id: int) -> Blog:
    r = requests.get(BASE_URL+"/blog/"+str(user_id))
    blog = Blog(**r.json())
    return blog


def get_article(article_id: str) -> Article:
    r = requests.get(BASE_URL+"/articles/"+article_id)
    return Article(**r.json())


def get_all_articles() -> list[Article]:
    r = requests.get(BASE_URL+"/articles/")
    articles = []
    for article in r.json():
        articles.append(Article(**article))
    return articles
