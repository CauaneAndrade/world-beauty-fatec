from django.contrib import admin
from django.urls import include, path

from world_beauty import beauty

urlpatterns = [
    path('', include('world_beauty.beauty.urls')),
    path('admin/', admin.site.urls),
]
