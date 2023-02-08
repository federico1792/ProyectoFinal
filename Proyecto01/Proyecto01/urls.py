from django.contrib import admin
from django.urls import path, include
from Proyecto01.views import index, about
from Proyecto01.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls'), name = 'include sales urls'),
    path('rentals/', include('rentals.urls'), name = 'include rentals urls'),
    path('users/', include('users.urls'), name = 'include users urls'),
    path('data/', include('data.urls'), name = 'include data urls'),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
