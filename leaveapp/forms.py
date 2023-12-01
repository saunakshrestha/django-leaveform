from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from leaveapp.models import LeaveRequest
from datetime import date
from accounts.models import User

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'department',
            'designation',
            'leave_from',
            'leave_to',
            'purpose_of_leave',
            'description'
        ]
    designation = forms.CharField(max_length=30)
    department = forms.ChoiceField(
        choices=LeaveRequest.DEPARTMENT_CHOICES
    )
    leave_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),initial=date.today())
    leave_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),initial=date.today())
    purpose_of_leave = forms.ChoiceField(choices=LeaveRequest.PURPOSE_OF_LEAVE_CHOICES)
    description = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        leave_from = cleaned_data.get("leave_from")
        leave_to = cleaned_data.get("leave_to")
        purpose_of_leave = cleaned_data.get("purpose_of_leave")
        description = cleaned_data.get("description")
        
        if leave_from > leave_to :
            self.add_error('leave_from','Leave from is in future.')
        if purpose_of_leave == 'others' and not description:
            self.add_error('description','Description is required')

        return cleaned_data
     
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
    password = forms.CharField(widget=forms.PasswordInput, max_length=128)

    def __init__(self,*args, **kwargs) :
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data=super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email',"Email already exists.")
        return cleaned_data