# from http.client import responses
#
# from django.shortcuts import render
# from .serializers import RegisterSerializer
# from django.contrib.auth import authenticate
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.request import Request
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from .tokens import create_jwt_pair
# from rest_framework.permissions import AllowAny
#
#
#
# # Create your views here.
# class RegisterStudentView(generics.CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer
#     def post(self,  request:Request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "New Student Registered Successfully",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         else:
#             response = {
#                 "message": "Failed To Register Student",
#                 "data": serializer.errors
#             }
#             return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
#
# class StudentLoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(request, email=email, password=password)
#
#         if user is not None:
#             tokens = create_jwt_pair(user)
#             response = {
#                 "message": "Student logged Successfully",
#                 "data": {
#                     "email": user.email,
#                     "tokens": tokens,
#                 }
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
#
#         response = {
#             "message": "Invalid credentials"
#         }
#         return Response(data=response, status=status.HTTP_401_UNAUTHORIZED)
#
#     def get(self, request: Request):
#         content = {
#             "user": str(request.user),
#             "auth": str(request.auth)
#         }
#         return Response(data=content, status=status.HTTP_200_OK)