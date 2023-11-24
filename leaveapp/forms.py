from django import forms
from leaveapp.models import LeaveRequest
from datetime import date
from django.contrib.auth.models import User

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'department',
            'designation',
            'leave_from',
            'leave_to',
            'purpose_of_leave',
        ]
    designation = forms.CharField(max_length=30)
    department = forms.ChoiceField(
        choices=LeaveRequest.DEPARTMENT_CHOICES
    )
    leave_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),initial=date.today())
    leave_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),initial=date.today())
    purpose_of_leave = forms.CharField(max_length=50)



    def clean(self):
        cleaned_data = super().clean()
        leave_from = cleaned_data.get("leave_from")
        leave_to = cleaned_data.get("leave_to")
        if leave_from > leave_to :
            raise forms.ValidationError("Error:'Leave from' date cannot be in future to 'Leave to' date.")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
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


    def clean(self):
        cleaned_data=super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if User.objects.filter(email=email).exists():
            self.add_error('email',"Email already exists.")
        return cleaned_data




class LeaveRequestEditForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'department',
            'designation',
            'leave_from',
            'leave_to',
            'purpose_of_leave',
        ]
        designation = forms.CharField(max_length=30)
        department = forms.ChoiceField(
            choices=LeaveRequest.DEPARTMENT_CHOICES
        )
        leave_from = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
        leave_to = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
        purpose_of_leave = forms.CharField(max_length=50)
