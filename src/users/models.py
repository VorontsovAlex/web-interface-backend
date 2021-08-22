import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4)
    email = models.CharField(max_length=255)
    phone = models.CharField(
        null=True, blank=True, max_length=30,
        verbose_name='Телефон',
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан', db_index=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен', db_index=True)

    objects = UserManager()

    @classmethod
    def parse_name(cls, name: str) -> dict:
        if name is None:
            return {}

        parts = name.split(' ', 2)

        if len(parts) == 1:
            return {'first_name': parts[0]}

        if len(parts) == 2:
            return {'first_name': parts[0], 'last_name': parts[1]}

        return {'first_name': parts[0], 'last_name': ' '.join(parts[1:])}

    def __str__(self):
        name = self.first_name + ' ' + self.last_name

        if len(name) < 3:
            return 'Anonymous'

        return name.strip()
