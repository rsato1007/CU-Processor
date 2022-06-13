from django.db import models
from django.contrib.auth.models import AbstractUser

# This class is part of Django and allows us to create
# an abstract user.
# Documentation can be found here: https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model
class User(AbstractUser):
    pass