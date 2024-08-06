from django import forms
from django.contrib.auth.models import User
from students.models import IssuedBook

class IssuedBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['student', 'book']
