"""DjangoGOvetDemo URL Configuration"""

from django.contrib import admin
from django.urls import path
from GOvetproject.urlshort import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]
