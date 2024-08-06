from django.db import models

from django.contrib.auth.models import User

class SchoolClass(models.Model):
    student_class = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)], unique=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Class {self.student_class}"
    
class User_Login(models.Model):
    role = models.CharField(max_length = 100,null=False,blank=False)
    username = models.CharField(max_length = 100,null=False,blank=False)
    password = models.CharField(max_length = 100,null=False,blank=False)
    email = models.EmailField(unique=True)

class Library(models.Model):
    book_name = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    student_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    book_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.book_name


# Create your models here.
