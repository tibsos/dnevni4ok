from django.urls import path
from .views import r,l,lo,p
urlpatterns=[
    path('register/',r,name='register'),
    path('login/',l,name='login'),
    path('logout/',lo,name='logout'),
    path('<str:username>/',p),
]