from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Green Home Admin"
admin.site.site_title = "Green Home Admin Portal"
admin.site.index_title = "Welcome to Green Home"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ap1.urls')),
    path('',include('ap2.urls')),
    path('',include('ap3.urls')),
    
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)