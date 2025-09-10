from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm_core.urls')),
    path('api/', include('crm_core.api_urls')),
]