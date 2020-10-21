"""GOvetproject URL Configuration"""

from django.contrib import admin
from django.urls import path
from GOvetproject.urlshort import views

urlpatterns = [
    path('shorten/', views.get_form, name='urlform'),  # If user submits a POST request get that
                                                        # information (URL) and encode it into a short URL
]
