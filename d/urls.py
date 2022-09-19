from django.urls import path
from .views import h,cd
urlpatterns=[
    path('',h),
    path('create-entry/',cd,name='create-entry'),
]