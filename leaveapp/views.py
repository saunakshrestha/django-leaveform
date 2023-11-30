from django.shortcuts import render, redirect, get_object_or_404
from leaveapp.forms import LeaveRequestForm,LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin
from django.contrib.auth.decorators import login_required
from leaveapp.models import LeaveRequest

@login_required(login_url='login_user')
def leave_request_submit(request):
    post_form = LeaveRequestForm(request.POST or None)
    if request.method == 'POST':
        post_form = LeaveRequestForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, "Your application submitted successfully.")
            return redirect('history')

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
                return redirect('history')
        messages.error(request,"Invalid Credentials")
        return render(request,'login.html',{'login_form':login_form})
    
def logout_user(request):
    logout(request)
    return redirect('login_user')


def register_user(request):
    context={}
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    elif request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            context['sweetalert']="Sweet"
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
            )
            user.set_password(password)
            user.is_active = False
            user.save()
            messages.success(request,"Your details are under verified. You'll be notified through email.")
            return redirect('register_user')
        else:
            messages.error(request,"Invalid credentials!")
    context['register_form']=register_form
    return render(request,'register.html',context)


@login_required(login_url='login_user')
def history(request):
    user = request.user
    if user.is_staff or user.is_superuser: 
        leave_request_data = LeaveRequest.objects.all().order_by('-id')
        print("isstaff")
    else:
        leave_request_data = LeaveRequest.objects.filter(user=user).order_by('-id')
        print("user opnly")

    context = {
        'leave_request_data':leave_request_data,
    }
    return render(request,'history.html',context)

@login_required(login_url='login_user')
def edit_leave_request(request,id):
    leave_request = get_object_or_404(LeaveRequest,id=id)
    edit_form = LeaveRequestForm(instance=leave_request)
    if request.method == 'POST':
        edit_form = LeaveRequestForm(request.POST,instance=leave_request)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,"The form has been successfully updated.")
            return redirect('history')
        else:
            messages.error(request,"Please! correct the errors:")
    else:
        edit_form = LeaveRequestForm(instance=leave_request)
    
    context = {
        'edit_form' : edit_form,
        'leave_request':leave_request,
    }
    return render(request,'edit_form.html',context)

@login_required(login_url='login_user')
def delete_leave_request(request,id):
    leave_request = get_object_or_404(LeaveRequest,id=id)
    leave_request.delete()
    messages.error(request,"The form has been deleted.")
    return redirect('history')

