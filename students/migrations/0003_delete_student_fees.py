# Generated by Django 4.2.8 on 2024-02-02 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_student_class_student_studentclass_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_Fees',
        ),
    ]