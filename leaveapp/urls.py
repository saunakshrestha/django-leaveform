
from leaveapp.views import *
from django.urls import path

urlpatterns = [
    path('leave/',leave_request_submit,name='leave_request'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user')
    
]