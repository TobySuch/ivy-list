from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # See https://stackoverflow.com/a/43209322
    USERNAME_FIELD = 'email'
    email = models.EmailField('email address', unique=True) # changes email to unique and blank to false
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS

