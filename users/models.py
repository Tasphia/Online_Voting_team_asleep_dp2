from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, nid, name, phone, password):
        if not nid:
            raise ValueError("Users must have a NID number")
        user = self.model(nid=nid, name=name, phone=phone, password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nid, name, phone, password):
        user = self.create_user(nid, name, phone, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Custom User Model
class User_db(AbstractBaseUser):
    name = models.CharField(max_length=100)
    nid = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)  # Password stored in plain text 
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nid'  # Login using NID
    REQUIRED_FIELDS = ['name', 'phone', 'password']

    objects = UserManager()

    def __str__(self):
        return self.name

