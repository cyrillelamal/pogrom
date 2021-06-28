# Создание геттеров и сеттеров для классов «запись», «комментарий»
# приложения «Гостевая книга». Создание функций для вывода на печать
# информации, хранящийся в объектах.
from datetime import datetime


class Inscription:  # ЗАЧЕМ?!
    def __init__(self, body: str, created_at: datetime):
        self._body = body
        self._created_at = created_at

    @property
    def body(self):
        return self._body

    @property
    def created_at(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    def __str__(self):
        return f"[{self.body}]-[{self.created_at}]-[]"


class Post(Inscription):
    def __init__(self, title: str, body: str, created_at: datetime):
        super().__init__(body, created_at)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


class Comment(Inscription):
    def __init__(self, body: str, created_at: datetime, post: Post):
        super().__init__(body, created_at)
        self._post = post

    @property
    def post(self):
        return self._post

    @post.setter
    def post(self, post: Post):
        self._post = post

    def __str__(self):
        string = super().__str__()
        return string + str(self.post)
