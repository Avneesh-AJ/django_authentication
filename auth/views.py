
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login,authenticate as authcheck
from django.contrib.auth.views import LoginView

from auth import forms

class Login(LoginView):
    template_name='auth/login.html'
    redirect_authenticated_user = True

# Create your views here.
"""""
def login(request):
    loginForm=forms.LoginForm()
    error=None
    if request.method=="POST":
        loginForm=forms.LoginForm(request.POST)
        if loginForm.is_valid():
            username=loginForm.cleaned_data['username']
            password=loginForm.cleaned_data['password']
            user=authcheck(username=username,password=password)
            if user:
                auth_login(request,user)
                return HttpResponseRedirect('/')
            else:
                error="Invalid credentials check user name and password"
                

    context={
        "form":loginForm,
        "error":error
    }
    return render(request,'auth/login.html',context)
"""