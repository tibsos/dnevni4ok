from django.contrib import admin as a
from .models import D,DE,F
a.site.register(F)
a.site.register(DE)
a.site.register(D)