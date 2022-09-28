from django.urls import path
from django.conf import settings as s
from .views import *
from d.views import p

app_label='u'

urlpatterns=[
    path('register/',r,name='register'),
    path('login/',l,name='login'),
    path('logout/',lo,name='logout'),
    path('<str:username>/',p),
]
