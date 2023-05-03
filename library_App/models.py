from django.db import models

from datetime import datetime
import uuid

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser

from library_App.managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField(unique=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        "User Permission to view the app 'app_label'."
        return True

    @property
    def is_staff(self):
        return self.is_admin 
        
    def __str__(self):
        return self.email


class Book(models.Model):

    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    upload_book = models.FileField(upload_to="uploads")
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title