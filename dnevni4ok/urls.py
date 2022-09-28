from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings as s

handler404 = 'dnevni4ok.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('d.urls')),
    path('settings/',include('s.urls')),
    path('',include('u.urls')),
]
urlpatterns += static(s.STATIC_URL, document_root=s.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(s.MEDIA_URL, document_root=s.MEDIA_ROOT)

