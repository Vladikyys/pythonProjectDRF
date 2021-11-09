from datetime import datetime, timedelta
import jwt
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    STATUS = (
        ('С', _('Customer')),
        ('E', _('Executor')),
    )
    objects = CustomUserManager()
    username = None
    email = models.EmailField(verbose_name='email', unique=True, null=True, max_length=100)
    status = models.CharField(max_length=1, choices=STATUS)
    first_name = models.CharField(max_length=120, blank=False)
    second_name = models.CharField(max_length=120, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return self.email
    #
    # @property
    # def token(self):
    #     """
    #     Позволяет получить токен пользователя путем вызова user.token, вместо
    #     user._generate_jwt_token(). Декоратор @property выше делает это
    #     возможным. token называется "динамическим свойством".
    #     """
    #     return self._generate_jwt_token()
    #
    # def get_full_name(self):
    #     """
    #     Этот метод требуется Django для таких вещей, как обработка электронной
    #     почты. Обычно это имя фамилия пользователя, но поскольку мы не
    #     используем их, будем возвращать username.
    #     """
    #     return self.first_name, self.last_name
    #
    # def get_short_name(self):
    #     return self.first_name
    #
    # def _generate_jwt_token(self):
    #     """
    #     Генерирует веб-токен JSON, в котором хранится идентификатор этого
    #     пользователя, срок действия токена составляет 1 день от создания
    #     """
    #     dt = datetime.now() + timedelta(days=1)
    #
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%S'))
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token
