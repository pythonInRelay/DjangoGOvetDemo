"""GOvetproject URL Configuration"""

from django.urls import path
from django.views.generic import RedirectView
from GOvetproject.urlshort import views

urlpatterns = [
    path('', RedirectView.as_view(url='/shorten/')),  # Redirect to shortener as it is the only app installed
    path('shorten/', views.get_form, name='urlform'),  # Get information (URL) and encode it into a short URL
    path('<short_url>/', views.redirect_short_url, name='redirect_function'),  # Redirect the user to short URL
]
