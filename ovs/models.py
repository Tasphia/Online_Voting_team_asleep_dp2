from django.db import models

class Nid_db(models.Model):
    nid = models.CharField(max_length=20, unique=True)
    name = models.TextField
    father_name=models.TextField
    mother_name=models.TextField
    DoB=models.DateField
    address=models.TextField
    phone_number=models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nid