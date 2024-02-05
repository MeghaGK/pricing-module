from django.contrib import admin
from django.urls import path, include
from pricing.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing.urls')),
    path('', home),
]
