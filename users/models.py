import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)

    # Это поле типа `UUIDField`, которое используется для генерации уникального идентификатора (UUID)
    # с помощью функции `uuid.uuid4()`.
    # Поле имеет значение по умолчанию `uuid.uuid4`,
    # что означает, что при создании нового пользователя будет автоматически сгенерирован уникальный ключ.
    # Опция `editable=False` указывает, что это поле нельзя изменять пользователем через административный интерфейс.
    verification_key = models.UUIDField(default=uuid.uuid4, editable=False)
    is_verified = models.BooleanField(default=False)

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
