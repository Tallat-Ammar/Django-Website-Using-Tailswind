# forms.py 
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee
  
class EmployeeForm(forms.ModelForm): 
  
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image'] 


class CreatUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
