from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import random, string
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def generate_matric_no(self):
        """Generate a random unique matric number like EDU2025-XXXXX"""
        prefix = "EDU"
        year = "2025"  # Or you can dynamically use timezone.now().year
        while True:
            random_digits = ''.join(random.choices(string.digits, k=5))
            matric = f"{prefix}{year}-{random_digits}"
            if not User.objects.filter(matric_no=matric).exists():
                return matric


class User(AbstractUser):
    username=None
    first_name=models.CharField(max_length=30, blank=False)
    last_name=models.CharField(max_length=30, blank=False)
    email=models.EmailField(unique=True, blank=False)
    phone_number=models.CharField(max_length=15, blank=False)
    matric_no=models.CharField(max_length=10, unique=True, blank=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    profile_pic=models.ImageField(upload_to="profiles/", null=True, blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", "matric_no"]

    objects = CustomUserManager()

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.email



