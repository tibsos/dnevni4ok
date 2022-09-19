from django.shortcuts import render,redirect
from u.models import P
from .forms import DF,DEF,FF
from .models import F
def h(request):
    c={}
    c['u']=request.user
    return render(request,'d/h.html',c)

def cd(request):
    # pass the diary if the entry was created in a diary

    if request.method=='POST':
        ff=FF(request.POST or None,request.FILES or None)
        files=request.FILES.getlist('f')
        if ff.is_valid():
            de=ff.save(commit=False)
            de.p=request.user.p
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