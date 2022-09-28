from django.contrib import admin as a
from .models import P,B,F

a.site.register(P)
a.site.register(B)
a.site.register(F)