from django.urls import path
from .views import *

app_name='d'

urlpatterns=[
    path('',h),
    path('udev/',udev,name='udev'),
    path('archive/',a,name='a'),
    #path('check-mention/',m,name='m'),
    path('create-entry/',cde,name='cde'),
    path('<uuid:uid>/edit/',ede),

]

htmx_urlpatterns=[
    path('f/',f,name='f'),
    path('a/',a,name='a'),
    path('el/',el,name='el'),
    path('rl/',rl,name='rl'),
    path('create-diary/',cd,name='cd'),
    path('de/<uuid:uid>/',de,name='de'),
    path('r/<uuid:uid>/',dr,name='dr'),
]

urlpatterns+=htmx_urlpatterns