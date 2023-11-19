
from leaveapp.views import *
from django.urls import path

urlpatterns = [
    path('',leave_request_submit,name='leave_request')
]