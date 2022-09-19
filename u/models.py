from django.db import models as m
from django.contrib.auth.models import User as U
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

def ua(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/a',s)
    
def ub(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/p/b',s)

class P(m.Model):
    P=(
        ('1','Public'),
        ('0','Public to followers'),
        ('-1','Private'),
    )
    u=m.OneToOneField(U,on_delete=m.CASCADE,related_name='p')

    n=m.CharField(_("Name"),max_length=150,blank=True,null=True)

    a=m.ImageField(_("Avatar"),upload_to=ua,default='d/a.jpg')
    b=m.ImageField(_("Banner"),upload_to=ub,blank=True,null=True)

    p=m.CharField(max_length=19,choices=P,default='1')
    sc=m.BooleanField(_("Confirmed Registration?"),default=False)
    
    def __str__(self):
        return self.u.username

    class Meta:    
        verbose_name='Profile'

@receiver(post_save,sender=U)
def update_p_signal(sender,instance,created,**kwargs):
    if created:
        P.objects.create(u=instance)
    instance.p.save()