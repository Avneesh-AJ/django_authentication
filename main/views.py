from cmath import log
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context={}
    return  render(request,'index.html')

@login_required(login_url='/auth/login')
def sshh(request):
    return HttpResponse("This is an authenticated view")
    
