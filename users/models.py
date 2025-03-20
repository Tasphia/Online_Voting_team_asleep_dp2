from django.db import models

# Custom User Model
class User(models.Model):
    name = models.CharField(max_length=100)
    nid = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'nid'  # Login using NID
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.name
