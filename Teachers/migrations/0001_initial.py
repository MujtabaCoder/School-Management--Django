# Generated by Django 4.2.8 on 2024-02-01 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administration', '0002_user_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('mobile', models.CharField(max_length=15)),
                ('joining_date', models.DateField()),
                ('qualification', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=255)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.schoolclass')),
            ],
        ),
    ]
