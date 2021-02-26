from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    year = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Upadted_at = models.DateTimeField(auto_now=True)

# Create your models here.
