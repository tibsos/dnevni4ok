from django.db import models as m
from django.utils.translation import gettext_lazy as _
from uuid import uuid4 as u4
import os
from u.models import P

def uf(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/d/f',s)
def uc(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/d/c',s)

class D(m.Model):
    p=m.ForeignKey(P,on_delete=m.CASCADE)
    t=m.CharField(_("Title"),max_length=150,blank=True,null=True)
    d=m.TextField(_("Description"),max_length=999,blank=True,null=True)
    c=m.FileField(_("Cover"),upload_to=uc,blank=True,null=True)
    ca=m.DateTimeField(_("Created At"),auto_now_add=True)
    ua=m.DateTimeField(_("Updated At"),auto_now=True)
    class Meta:
        verbose_name='Diary'
        verbose_name_plural='Diaries'
        ordering=['ua']

class DE(m.Model):
    C=(
        ('#aaa','Black'),
        ('#fff','White'),
    )
    uid=m.UUIDField(default=u4)
    a=m.ForeignKey(P,on_delete=m.CASCADE)
    # Content
    t=m.CharField(_("Title"),max_length=150,blank=True,null=True)
    c=m.TextField(_("Content"),max_length=999,blank=True,null=True)
    # Personal

    ## Pinned

    # Appearance
    cr=m.CharField(_("Color"),max_length=10,choices=C)
    b=m.FileField(_("Background"),upload_to=uc,blank=True,null=True)
    
    # Sharing

    # DateTimes
    ca=m.DateTimeField(_("Created At"),auto_now_add=True)
    ua=m.DateTimeField(_("Updated At"),auto_now=True)
    
    def __str__(self):
        return self.t + " by " + str(self.a)

    class Meta:
        verbose_name='Diary Entry'
        verbose_name_plural='Diary Entries'
        ordering=['ua']

class F(m.Model):
    e=m.ForeignKey(DE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    f=m.FileField(_("File"),upload_to=uf,)
    aa=m.DateTimeField(_("Added At"),auto_now_add=True)
    
    def __str__(self):
        return self.e.t

    class Meta:
        verbose_name='File'
        ordering=['aa']