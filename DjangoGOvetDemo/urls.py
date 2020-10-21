"""DjangoGOvetDemo URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from GOvetproject.urlshort import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GOvetproject.urlshort.urls'))  # Redirect to shortener as it is the only app installed
]
