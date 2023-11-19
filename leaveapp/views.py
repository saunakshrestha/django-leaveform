from django.shortcuts import render, redirect
from leaveapp.forms import LeaveRequestForm
from django.contrib import messages

def leave_request_submit(request):
    post_form = LeaveRequestForm()
    if request.method == 'POST':
        post_form = LeaveRequestForm(request.POST)
        if post_form.is_valid():
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

    return render(request, 'index.html', context)
