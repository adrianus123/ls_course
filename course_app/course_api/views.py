from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer, CourseReportSerializer


# Create your views here.
class CourseView(APIView):
    def get(self, request):
        category = request.query_params.get("category", None)
        course = Course.objects.all()

        if category is not None:
            course = course.filter(category_id=category)

        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        enrollment = Enrollment.objects.filter(user=user_id)

        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(enrollment, request)

        serializer = EnrollmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CourseReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        role = request.user.user_role
        user_id = request.user.id
        course = request.query_params.get("course", None)

        enrollment = Enrollment.objects.all().order_by("-grade", "user__fullname", "user_id")

        if role != "admin":
            enrollment = enrollment.filter(user=user_id)

        if role == "admin" and course is not None:
            enrollment = enrollment.filter(course=course)

        serializer = CourseReportSerializer(enrollment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
