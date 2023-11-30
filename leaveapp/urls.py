
from leaveapp.views import *
from django.urls import path

urlpatterns = [
    path('',leave_request_submit,name='leave_request'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('register/',register_user,name='register_user'),
    path('dashboard/',dashboard,name='dashboard'),
    path('edit_form/<int:id>/',edit_leave_request,name='edit_form'),
    path('delete_form/<int:id>/',delete_leave_request,name='delete_form')
]
