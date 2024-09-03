from django.urls import path
from .views import CourseView, EnrollmentView, CourseReportView

urlpatterns = [
    path("list", CourseView.as_view()),
    path("enrollment", EnrollmentView.as_view()),
    path("report", CourseReportView.as_view()),
]
