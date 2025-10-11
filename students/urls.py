from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("register/", views.RegisterStudentView.as_view(), name="register_student"),
    path("login/", views.StudentLoginView.as_view(), name="student_login"),

]