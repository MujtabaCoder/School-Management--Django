# Generated by Django 4.2.8 on 2024-02-01 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
    ]