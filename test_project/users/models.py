from django.contrib.auth.models import AbstractUser
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
    email = models.EmailField(_('email address'), unique=True)

    status = models.CharField(max_length=1, choices=STATUS)
    first_name = models.CharField(max_length=120, blank=False)
    second_name = models.CharField(max_length=120, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
