from django.db import models
from django.db import models
from datetime import datetime
from Administration.models import SchoolClass,Library
from datetime import datetime,timedelta




class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    roll = models.CharField(max_length=20, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    religion = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    section = models.CharField(max_length=5, blank=True, null=True)
    admission_id = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    studentclass=models.ForeignKey(SchoolClass,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name)

# class Student_Fees(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     payment_date = models.DateField()
#     pay_amt = models.DecimalField(max_digits=10, decimal_places=2)
#     outstanding_amt = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_mode = models.CharField(max_length=20)  # You may want to use choices for specific payment modes
#     next_pd = models.DateField()

#     def __str__(self):
#         return f"{self.student.first_name} {self.student.last_name} - Fees Record"
def get_expiry():
    return datetime.today() + timedelta(days=15)
class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Library, on_delete=models.CASCADE)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return str(self.student)

