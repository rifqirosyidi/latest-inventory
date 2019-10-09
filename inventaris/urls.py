from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # App Urls
    path('', include('inventarisir.urls')),

    # API Urls
    path('api/', include('inventarisir.api.urls'))
]
