from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login as auth_login

def register(request):
    redirect_to = request.POST.get('next',request.GET.get('next',''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            auth_login(request, user)
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',context={'form':form, 'next':redirect_to})
