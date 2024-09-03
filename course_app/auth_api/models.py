from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    fullname = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=255, blank=False)
    user_role = models.CharField(max_length=50, blank=False)
    course = models.ManyToManyField(
        "course_api.Course", through="course_api.Enrollment"
    )
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
