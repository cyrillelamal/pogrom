# Разработка классов и объектов «запись», «комментарий» для приложения
# «Блог» (использование наследования).
from datetime import datetime


class Inscription:  # ЗАЧЕМ?!
    pass


class Post(Inscription):
    def __init__(self, title: str, body: str, created_at: datetime):
        self.body = body
        self.title = title
        self.created_at = created_at


class Comment(Inscription):
    def __init__(self, text: str, created_at: datetime, post: Post):
        self.post = post
        self.text = text
        self.created_at = created_at
