from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    first_name: str
    last_name: str


class BlogSubscriber(BaseModel):
    id: int
    subscriber: str
    blog: str


class Article(BaseModel):
    id: str
    author: str
    category: str
    blog: str
    title: str
    text: str
    # Временное решение
    posted_date: str
    edited_date: str


class Blog(BaseModel):
    id: str
    owner: str
    category: list[str]
    blogsubscribers: list[BlogSubscriber]
    articles: list[Article]
    name: str
