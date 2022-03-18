from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from library.models import *
# Create your models here.
from .managers import CustomUserManager


class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField (_ ('email address'), unique=True)
    first_name = models.CharField (max_length=20)
    last_name = models.CharField (max_length=20)
    street_num = models.CharField (max_length=20)
    state = models.CharField (max_length=2)
    zipcode = models.IntegerField (null=True)
    city = models.CharField (max_length=20)
    is_staff = models.BooleanField (default=False)
    is_active = models.BooleanField (default=True)
    date_joined = models.DateTimeField (default=timezone.now)
    favorite_books = models.ManyToManyField (Book, related_name='favorite_books', blank=True)
    favorite_genres = models.ManyToManyField (Genre, related_name='favorite_genres', blank=True)
    favorite_authors = models.ManyToManyField (Author, related_name='favorite_authors', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager ( )

    def __str__(self):
        return self.email


