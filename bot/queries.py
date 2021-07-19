import os
import dotenv

import requests

from .models import Article, Blog, UserCreate, UserGet


dotenv.load_dotenv()
BASE_URL = str(os.getenv("BASE_URL"))


def create_user(user: UserCreate) -> int:
    r = requests.post(BASE_URL+"/users/", data=user.dict())
    return r.status_code


def get_user(user_id: int):
    r = requests.get(BASE_URL+"/users/"+str(user_id))
    user = UserGet(**r.json())
    return user


def get_blog(user_id: int) -> list[Blog]:
    r = requests.get(BASE_URL+"/blog/"+str(user_id))
    blogs = []
    if len(r.json()) > 1:
        for blog in r.json():
            blogs.append(Blog(**blog))
    else:
        blogs.append(Blog(**r.json()[0]))
    return blogs


def get_article(article_id: str) -> Article:
    r = requests.get(BASE_URL+"/articles/"+article_id)
    return Article(**r.json())


def get_all_articles() -> list[Article]:
    r = requests.get(BASE_URL+"/articles/")
    articles = []
    for article in r.json():
        articles.append(Article(**article))
    return articles
