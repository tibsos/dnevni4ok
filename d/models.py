from django.db import models as m
from django.utils.translation import gettext_lazy as _
from uuid import uuid4 as u4
import os
from u.models import P
from django.shortcuts import reverse

def uf(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/d/f',s)
def uc(instance,filename):
    e=filename.split('.')[-1]
    s="%s.%s"%(u4,e)
    return os.path.join('u/d/c',s)

class D(m.Model):
    a=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Author')
    t=m.CharField(_("Title"),max_length=150,blank=True,null=True)
    d=m.TextField(_("Description"),max_length=999,blank=True,null=True)
    c=m.FileField(_("Cover"),upload_to=uc,blank=True,null=True)
    ca=m.DateTimeField(_("Created At"),auto_now_add=True)
    ua=m.DateTimeField(_("Updated At"),auto_now=True)
    
    def __str__(self):
        return self.t or ''
    
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
    a=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Author')
    d=m.ForeignKey(D,on_delete=m.CASCADE,blank=True,null=True,verbose_name='Diary')
    # Content
    t=m.CharField(_("Title"),max_length=150,blank=True,null=True)
    c=m.TextField(_("Content"),max_length=999,blank=True,null=True)
    # Personal
    h=m.BooleanField(_("Archived?"),default=False)
    ## Pinned

    # Appearance
    b=m.FileField(_("Background"),upload_to=uc,blank=True,null=True)
    
    # Sharing

    l=m.ManyToManyField('EL',blank=True,verbose_name='Likes ')
    v=m.PositiveIntegerField(_("Entry views"),default=0)

    # DateTimes
    ca=m.DateTimeField(_("Created At"),auto_now_add=True)
    ua=m.DateTimeField(_("Updated At"),auto_now=True)
    
    def __str__(self):
        return self.t

    def get_absolute_url(self):
            return reverse("ede", kwargs={"uid": self.uid})

    class Meta:
        verbose_name='Diary Entry'
        verbose_name_plural='Diary Entries'
        ordering=['ua']

class F(m.Model):
    e=m.ForeignKey(DE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    f=m.FileField(_("File"),upload_to=uf)
    aa=m.DateTimeField(_("Added At"),auto_now_add=True)
    
    def __str__(self):
        return self.e.t

    class Meta:
        verbose_name='File'
        ordering=['aa']

class RE(m.Model):
    uid=m.UUIDField(default=u4)
    de=m.ForeignKey(DE,on_delete=m.CASCADE,related_name='reposted_post')
    a=m.ForeignKey(P,on_delete=m.CASCADE)
    t=m.CharField(_("Text"),max_length=333,blank=True,null=True)

    h=m.BooleanField(_("Archive?"),default=False)

    l=m.ManyToManyField('RL',blank=True)
    v=m.PositiveIntegerField(_("Entry views"),default=0)

    ca=m.DateTimeField(_("Created At"),auto_now_add=True)
    ua=m.DateTimeField(_("Updated At"),auto_now=True)
    def __str__(self):
        return "'"+(str(self.de.t)+"'" + " reposted by " + "@"+str(self.a.u.username))

    class Meta:
        verbose_name='Reposted Diary'
        verbose_name_plural='Reposted Diaries'
        ordering=['-ca']

class EL(m.Model):
    e=m.ForeignKey(DE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Liking Profile')
    la=m.DateTimeField(_("Liked At"),auto_now_add=True)
    
    def __str__(self):
        return (self.p.u.username+" likes "+self.e.t) or ''

    class Meta:
        verbose_name='Entry Like'
        ordering=['la']
class RL(m.Model):
    e=m.ForeignKey(DE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Liking Profile')
    la=m.DateTimeField(_("Liked At"),auto_now_add=True)
    
    def __str__(self):
        return self.p.u.username+" likes "+self.e.t

    class Meta:
        verbose_name='Repost Like'
        ordering=['la']

class ECL(m.Model):
    e=m.ForeignKey('EC',on_delete=m.CASCADE,verbose_name='Comment')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Liking Profile')
    la=m.DateTimeField(_("Liked At"),auto_now_add=True)
    
    def __str__(self):
        return self.p.u.username+" likes comment by "+self.e.e.a.u.username+" '"+self.e.c+"'"

    class Meta:
        verbose_name='Entry Like'
        ordering=['la']

class EC(m.Model):
    uid=m.UUIDField(default=u4)
    r=m.ForeignKey('EC',on_delete=m.DO_NOTHING,verbose_name='Reply to comment')
    e=m.ForeignKey(DE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Commenting Profile')
    c=m.TextField(_("Comment"),max_length=300)
    l=m.ManyToManyField(ECL,blank=True,verbose_name='Comment Likes')
    ca=m.DateTimeField(_("Commented At"),auto_now_add=True)
    ea=m.DateTimeField(_("Edited At"),auto_now=True)
    
    def __str__(self):
        return self.p.u.username+" commented on "+self.e.t +" '"+self.c+"'"

    class Meta:
        verbose_name='Entry Comment'
        ordering=['ca']

class RCL(m.Model):
    e=m.ForeignKey('RC',on_delete=m.CASCADE,verbose_name='Comment')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Liking Profile')
    la=m.DateTimeField(_("Liked At"),auto_now_add=True)
    
    def __str__(self):
        return self.p.u.username+" likes comment by "+self.e.e.a.u.username+" '"+self.e.c+"'"

    class Meta:
        verbose_name='Repost Like'
        ordering=['la']

class RC(m.Model):
    uid=m.UUIDField(default=u4)
    r=m.ForeignKey('RC',on_delete=m.DO_NOTHING,verbose_name='Reply to comment')
    e=m.ForeignKey(RE,on_delete=m.CASCADE,verbose_name='Diary Entry')
    p=m.ForeignKey(P,on_delete=m.CASCADE,verbose_name='Commenting Profile')
    c=m.TextField(_("Comment"),max_length=300)
    l=m.ManyToManyField(ECL,blank=True,verbose_name='Comment Likes')
    ca=m.DateTimeField(_("Commented At"),auto_now_add=True)
    ea=m.DateTimeField(_("Edited At"),auto_now=True)
    
    def __str__(self):
        return self.p.u.username+" commented on "+self.e.t +" '"+self.c+"'"

    class Meta:
        verbose_name='Entry Comment'
        ordering=['ca']