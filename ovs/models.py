from django.db import models

class User(models.Model):
    nid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.nid