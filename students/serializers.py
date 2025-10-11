from rest_framework import serializers
from .models import User
import random
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token



class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=100, min_length=6, write_only=True)
    phone_number = serializers.CharField(max_length=15)
    matric_no = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password', 'matric_no']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError("Email already exists, please use another email")

        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        matric_no = f"EDU/{random.randint(10000, 99999)}"
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data, matric_no=matric_no)
        Token.objects.create(user=user)
        return user

        return user