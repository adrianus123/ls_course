from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    title = models.CharField(max_length=255, blank=False)
    trainer = models.CharField(max_length=100, blank=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField(blank=False, default=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey('auth_api.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)
    grade = models.DecimalField(max_digits=3, decimal_places=1)
