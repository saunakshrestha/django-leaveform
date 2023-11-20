from django import forms
from leaveapp.models import LeaveRequest
from datetime import date

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

