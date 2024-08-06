from django.db import models
from Administration.models import SchoolClass


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=15)
    joining_date = models.DateField()
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    student_class=models.ForeignKey(SchoolClass,on_delete=models.CASCADE)

# Create your models here.
