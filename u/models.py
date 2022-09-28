from django.db import models as m
from django.contrib.auth.models import User as U
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from uuid import uuid4 as u4
import os
from django.urls import reverse

def ua(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/a',s)

def ub(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/b',s)

class B(m.Model):

    uid=m.UUIDField(default=u4)
    u=m.ForeignKey(U,on_delete=m.CASCADE,related_name='bc',blank=True,null=True)
    #p=m.BooleanField(_("Premium?"),default=False)
    i=m.ImageField(upload_to=ub)
    ca=m.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Banner'
        ordering=['ca']


class P(m.Model):
    P=(
        ('1','Public'),
        ('0','Public to followers'),
        ('-1','Private'),
    )
    u=m.OneToOneField(U,on_delete=m.CASCADE,related_name='p')

    n=m.CharField(_("Name"),max_length=150,blank=True,null=True)

    a=m.ImageField(_("Avatar"),upload_to=ua,default='d/a.jpg')
    b=m.ForeignKey(B,on_delete=m.DO_NOTHING,blank=True,null=True,related_name='pb') # Change b4 production

    #pr=m.CharField(_("Pronoun"),max_length=10,choices=PRONOUNS)

    p=m.CharField(max_length=19,choices=P,default='1')
    sc=m.BooleanField(_("Confirmed Registration?"),default=False)
    
    def __str__(self):
        return self.u.username

    def get_absolute_url(self):
        return reverse("p", kwargs={"username": self.u.username})
    

    class Meta:    
        verbose_name='Profile'

@receiver(post_save,sender=U)
def update_p_signal(sender,instance,created,**kwargs):
    if created:
        P.objects.create(u=instance)
    instance.p.save()


class F(m.Model):

    f=m.ForeignKey('P',on_delete=m.CASCADE,verbose_name='Follower',related_name='follower_profile')
    p=m.ForeignKey('P',on_delete=m.CASCADE,verbose_name='Followed Profile',related_name='following_profile')
    fa=m.DateTimeField(_("Followed At"),auto_now_add=True)

    def __str__(self):
        return str(self.f.u) +" is following " +str(self.p.u)

    class Meta:
        ordering=['-fa']
        verbose_name='Follower'