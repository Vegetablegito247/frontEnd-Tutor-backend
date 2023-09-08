from django.db import models
from .custom import customiseFrontenders
from django.contrib.auth.models import AbstractUser

# Create your models here.
class FrontendUsers(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length= 255, blank=True)
    contact = models.CharField(max_length=11, blank=True)
    otherName = models.CharField(max_length= 255, blank=True, null=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length= 255, blank=True, null=True)

    objects = customiseFrontenders()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []