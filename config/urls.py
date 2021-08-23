from index import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('', views.index, name='index'),
    path('psbo/', include('psbo.urls')),
    path('common/', include('common.urls')),
]
