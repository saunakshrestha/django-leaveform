from django.contrib import admin
from accounts.models import User
from leaveapp.models import LeaveRequest
# Register your models here.



@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'leave_applied_date',
        'total_leave_days',
        'approved_by_supervisor',
    ]
    readonly_fields = ["total_leave_days","signature_of_applicant","leave_applied_date","name"]



