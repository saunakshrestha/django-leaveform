from django.shortcuts import render, redirect
from leaveapp.forms import LeaveRequestForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_user')
def leave_request_submit(request):
    

    post_form = LeaveRequestForm()
    if request.method == 'POST':
        post_form = LeaveRequestForm(request.POST)
        if post_form.is_valid():
            post_form.instance.user = request.user
            
            post_form.save()
            messages.success(request, "Your application submitted sucesfully.")
            return redirect('leave_request')
        else:
            errors = post_form.errors.get('__all__')
            for error in errors:
                messages.error(request, error)
            post_form = LeaveRequestForm()        

    context = {
        'post_form': post_form,
        
    }

    return render(request, 'form.html', context)

def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'login.html',{'login_form':login_form})
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            if not User.objects.filter(username=username).exists():
                messages.error(request,"Invalid Username")
            user = authenticate(request=request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f"{username.title()},welcome back!")
                return redirect('leave_request')
        messages.error(request,f"Invalid Password")
        return render(request,'login.html',{'login_form':login_form})
    
def logout_user(request):
    logout(request)
    return redirect('login_user')

