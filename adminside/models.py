from django.db import models
from django.forms import ModelForm
from django import forms
# Create your models here.

class rgsrform(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to='./media/',default='')

class rgsrModelForm(forms.ModelForm):
    class Meta:
        model = rgsrform
        fields = ["fullname","email","password","image"]