import email
from enum import unique
from django.db import models

# Create your models here.
class student_info(models.Model):
    name = models.CharField(max_length=30)
    sid = models.IntegerField()
    email = models.EmailField()
    program = models.CharField(max_length=20)

    def __str__(self):
        return self.name