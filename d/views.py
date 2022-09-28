from django.shortcuts import render,redirect,get_object_or_404
from u.models import P
from d.models import DE
from .forms import DF,DEF,FF
from u.models import F as Fo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as U
from .models import D,DE,RE,F,EL,RL
from .forms import DF,DEF

from itertools import chain
from operator import attrgetter
from django.http import JsonResponse

# Pages

def h(request):
    return render(request,'d/l.html')

def a(r):

    u=r.u
    p=P.objects.get(u=u)

    e=DE.objects.filter(a=p).filter(d=None).filter(x=True)
    re=RE.objects.filter(a=p).filter(h=True)
    e=sorted(chain(e,re),key=attrgetter('ca'),reverse=True)

    c['p'],c['e']=p,e
    return render(r,'n/a.html')

def udev(r):
    de=DE.objects.filter(uid=r.POST['uid'])[0]
    if de is not None:
        de.v+=1
        de.save()
    return JsonResponse({})

def p(r,username):
    c={}
    u = get_object_or_404(U,username=username)
    p=P.objects.get(u=u)
    d=D.objects.filter(a=p)
    e=DE.objects.filter(a=p).filter(d=None).filter(h=False)
    re=RE.objects.filter(a=p).filter(h=False)
    e=sorted(chain(e,re),key=attrgetter('ca'),reverse=True)
    f=Fo.objects.filter(f=p,p=r.user.p)
    if len(f)>0:
        c['f']=True
    else:
        c['f']=False

    c['l']=True

    ap=P.objects.all()

    c['p'],c['d'],c['e'],c['ap'],c['u']=p,d,e,ap,u

    if u==r.user:
        if r.method=='POST' and "create-entry" in r.POST:
            DEf=DEF(r.POST or None)
            if DEf.is_valid():
                de=DEf.save(commit=False)
                de.a=r.user.p
                de.save()

        return render(r,'u/ep.html',c)
    else:
        if r.method=='POST' and 'repost' in r.POST:
            t=r.POST.get('repostText',False)
            de=r.POST.get('postToRepost', False)
            a=r.user.p
            de=DE.objects.filter(uid=de)[0]
            RE.objects.create(a=a,t=t,de=de)
        return render(r,'u/p.html',c)

# P methods

def f(r):
    u=r.user
    p=P.objects.get(u=u)
   
    pr=r.POST
    f=pr.get('p')
    f=U.objects.get(username=f)
    u = f
    c=Fo.objects.filter(p=p,f=f.p)
    if len(c)>0:
        c.delete()
        f=False
    else:
        Fo.objects.create(p=p,f=f.p)
        f=True

    x={}
    x['f'],x['u']=f,u

    return render(r,'u/ep/fb.html',x)

def el(r):

    u=r.user
    p=P.objects.get(u=u)


    uid=r.POST.get('entryUID')
    print(uid)
    e=DE.objects.get(uid=uid)

    c={}
    
    # check if already liked and act accordingly

    if len(EL.objects.filter(e=e,p=p))>0:
        c['l']=True
        EL.objects.filter(e=e,p=p)[0].delete()
    else:
        EL.objects.create(e=e,p=p)
        c['l']=False

    # return number of post likes
    #c['e']=len(EL.objects.filter(uid=uid))

    return render(r,'u/p/del.html',c)
def rl(r):

    u=r.user
    p=P.objects.get(u=u)


    uid=r.POST.get('e')
    e=RE.objects.get(uid=uid)

    c={}

    RL.objects.create(e=e,p=p)
    c['e']=len(RL.objects.filter(uid=uid))

    return render(r,'u/p/del.html',c)


def dr(r,uid):
    RE.objects.filter(uid=uid).delete()
    u = r.user
    p=P.objects.get(u=u)
    d=D.objects.filter(a=p)
    e=DE.objects.filter(a=p).filter(d=None)
    re=RE.objects.filter(a=p)
    e=sorted(chain(e,re),key=attrgetter('ca'))

    c={}
    c['p'],c['d'],c['e']=p,d,e

    if u==r.user:
        if r.method=='POST' and "create-entry" in r.POST:
            DEf=DEF(r.POST or None)
            if DEf.is_valid():
                de=DEf.save(commit=False)
                de.a=r.user.p
                de.save()


        return render(r,'u/ep.html',c)

# EP methods

def cd(r):
    
    u=r.user
    p=P.objects.get(u=u)
   
    pr=r.POST
    t,dd=pr.get('dt'),pr.get('dd')
    d=D.objects.create(a=p,t=t,d=dd)

    d=D.objects.filter(a=p)
    c={'d':d}

    return render(r,'u/ep.html',c)

def ede(r):
    return render(r,'d/ede.html')

def de(r,uid):
    DE.objects.filter(uid=uid).delete()
    u = r.user
    p=P.objects.get(u=u)
    d=D.objects.filter(a=p)
    e=DE.objects.filter(a=p).filter(d=None)
    re=RE.objects.filter(a=p)
    e=sorted(chain(e,re),key=attrgetter('ca'))

    c={}
    c['p'],c['d'],c['e']=p,d,e

    if u==r.user:
        if r.method=='POST' and "create-entry" in r.POST:
            DEf=DEF(r.POST or None)
            if DEf.is_valid():
                de=DEf.save(commit=False)
                de.a=r.user.p
                de.save()
        elif r.method=='POST' and "create-diary" in r.POST:
            
            df=DF(r.POST or None)
            if df.is_valid():
                d=df.save(commit=False)
                d.a=r.user.p
                d.save()

        c['df'],c['def']=DF(),DEF()

        return render(r,'u/ep.html',c)


def cde(request):
    # pass the diary if the entry was created in a diary

    if request.method=='POST':
        ff=FF(request.POST or None,request.FILES or None)
        files=request.FILES.getlist('f')
        if ff.is_valid():
            de=ff.save(commit=False)
            de.a=request.user.p
            de.save()
            if files:
                for f in files:  
                    F.objects.create(e=de,f=f)
            else:
                print('n')
            return redirect('/')
    else:
        ff=FF()
    c={}
    c['def'],c['ff']=DEF,FF
    return render(request,'d/cd.html',c)

def a(r):
    c={}
    return render(r,'u/p/a.html',c)