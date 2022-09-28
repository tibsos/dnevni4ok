from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm as AF

from .forms import RF

from django.contrib.auth.models import User as U
from .models import P
from d.models import D,DE,RE
from d.forms import DF,DEF

from itertools import chain
from operator import attrgetter


def l(request):
    if request.method=='POST':
        f=AF(request,data=request.POST)
        if f.is_valid():
            username=f.cleaned_data.get('username')
            password=f.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')  
                  
        else:
            messages.error(request,"Invalid username/pword")
    else:
        f=AF()
    c={}
    c['f']=f
    return render(request,'a/l.html',c)

def lo(r):
    logout(r)
    return redirect('/')

def r(r):
    if r.method == 'POST':
        f=RF(r.POST)
        if f.is_valid():
            u=f.save()
            u.refresh_from_db()
            user=authenticate(username=f.cleaned_data.get('username'),password=f.cleaned_data.get('password1'))
            login(r,user)
            return redirect('/')
    else:
        f=RF()
    c={}
    c['f']=f
    return render(r,'a/r.html',c)


