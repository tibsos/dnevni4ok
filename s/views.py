from django.shortcuts import render 
from u.models import B
from django.contrib.auth.models import User as U
from .f import *


def p(r):

    u=r.user
    p=u.p

    # Banner Form
    db=B.objects.filter(u=None)

    if r.method=='POST' and "defaultBanners" in r.POST:
        b=r.POST.get('selectedBanner', False)
        sb=B.objects.filter(uid=b)
        p.b=sb[0]
        p.save()
    

    c={}
    c['p'],c['db'],c['bf']=p,db,BF
    return render(r,'s/p.html',c)


"""     if r.method=='POST':
        bf=BF(r.POST)
    else:
        bf=BF() """