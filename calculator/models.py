#from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, phone, password=None):
        """Create a new user"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, phone, password):
        """Create a new superuser"""
        user = self.create_user(email, name, phone, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def get_user_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_user_phone(self):
        """Retrieve phone number of user"""
        return self.phone

    def __str__(self):
        """Return string representation of user"""
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of category"""
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    overview = models.CharField(max_length=1023)
    price = models.IntegerField()
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    language = models.CharField(max_length=255)
    instructor = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Return string representation of a course"""
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    reading_time = models.IntegerField()
    views = models.IntegerField()
    description = models.CharField(max_length=511)
    text = models.TextField()
    author = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """Return string representation of article"""
        return self.author.get_user_name() + "'s article on " + self.name

class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo_path = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of partner"""
        return self.name
#class Grade (models.Model):
    #course_code = models.CharField(max_length =10,unique =True , null = False)
    #course_name = models.CharField(max_length =250,unique =True , null = False)
    #grade = models.DecimalField(max_digits=3, decimal_places=1)

#class student(models.Model):
    #student_id = models.IntegerField(unique =True , null = False)
    #first_name = models.CharField(max_length=255)
    #last_name = models.CharField(max_length =100, null = False)
    #grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
    #semester = models.CharField(max_length =2,null = False)







# Create your models here.
