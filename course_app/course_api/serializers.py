from rest_framework import serializers
from .models import Course, Category, Enrollment
from auth_api.serializers import UserSerializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ["id", "title", "trainer", "rating", "price", "quantity", "category"]


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ["id", "user", "course", "enrollment_date"]


class CourseReportSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ["id", "user", "course", "grade"]
