from django import forms
from leaveapp.models import LeaveRequest
from datetime import date

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = [
            'name',
            'department',
            'designation',
            'leave_from',
            'leave_to',
            'purpose_of_leave',
        ]
    
    name = forms.CharField(
    label='Name',
    max_length=30,
    widget=forms.TextInput(attrs={'placeholder': 'Enter your full name:'})
    )
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