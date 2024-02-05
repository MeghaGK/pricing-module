from django.urls import path
from .views import calculate_pricing
from .views import home

urlpatterns = [
    # str is used to consider parameters of data type float
    path('calculate-pricing/<str:distance>/<str:time>/<str:waiting_time>/', calculate_pricing),
]
