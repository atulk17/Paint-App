from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from paint import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paint.urls')),
   
]