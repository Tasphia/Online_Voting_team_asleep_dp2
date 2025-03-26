from django.db import models

class Nid_db(models.Model):
    nid = models.CharField(max_length=20, unique=True)
    name = models.TextField(default="Unknown")
    father_name = models.TextField(default="Unknown")
    mother_name = models.TextField(default="Unknown")
    DoB = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, default="Unknown")
    phone_number = models.CharField(max_length=15, unique=True, default="0000000")
    
    def __str__(self):
        return self.nid

class User(models.Model):
    name = models.CharField(max_length=100)
    nid = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)  # Password stored in plain text 
    

    def __str__(self):
        return self.name
