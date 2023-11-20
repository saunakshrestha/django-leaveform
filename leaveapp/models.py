from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class LeaveRequest(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT','Information Technology'),
        ('HR','Human Resource'),
        ('BS','Business'),
    ]
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    department = models.CharField(max_length=30,choices=DEPARTMENT_CHOICES)
    leave_from = models.DateField()
    leave_to = models.DateField()
    total_leave_days = models.IntegerField(default=0)
    purpose_of_leave = models.CharField(max_length=50)
    leave_applied_date = models.DateField(auto_now_add=True)
    signature_of_applicant = models.CharField(max_length=30)
    approved_by_supervisor = models.BooleanField(default=False)
    approved_by_hr = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.name}:{self.leave_from} to {self.leave_to}"
    def save(self, *args, **kwargs):
        self.total_leave_days = (self.leave_to - self.leave_from).days + 1
        self.name = f"{self.user.first_name} {self.user.last_name}"
        self.signature_of_applicant = self.name
        super().save(*args,**kwargs)
