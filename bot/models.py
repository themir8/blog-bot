from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: int
    username: str
    first_name: str
    last_name: str


class BlogSubscriber(BaseModel):
    id: int
    subscriber: int
    blog: list[str]


class UserGet(BaseModel):
    id: int
    follows: BlogSubscriber
    user_id: int
    username: str
    first_name: str
    last_name: str


class Article(BaseModel):
    id: str
    author: int
    category: int
    blog: str
    title: str
    text: str
    # Временное решение
    posted_date: str
    edited_date: str


class Blog(BaseModel):
    id: str
    owner: int
    category: list[int]
    blogsubscribers: list[BlogSubscriber]
    articles: list[Article]
    name: str
