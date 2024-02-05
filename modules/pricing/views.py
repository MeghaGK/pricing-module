from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from django.shortcuts import get_object_or_404
from .models import PricingConfiguration
from decimal import Decimal

def calculate_pricing(request, distance, time, waiting_time):
    try:
        # API to calculate the pricing 
        # distance, time, and waiting_time are received from the request
        # select the active pricing module
        active_config = get_object_or_404(PricingConfiguration, is_active=True)
        distance = Decimal(distance)
        time = Decimal(time)
        waiting_time = Decimal(waiting_time)


        # pricing calculation logic based on the formula provided
        # distance - additional distance traveled
        if distance > active_config.base_distance:
            additional_distance = distance - active_config.base_distance
        else:
            additional_distance = 0
        if waiting_time >  active_config.base_wc:
            waiting_time = waiting_time - active_config.base_wc
        else:
            waiting_time = 0
        price = (active_config.dbp + (additional_distance * active_config.dap)) + (time * active_config.tmf) + (waiting_time * active_config.wc)
        return JsonResponse({"price": price})

    except Exception as e:
        print(e)
        return HttpResponseServerError("Internal Server Error")


def home(request):
    return HttpResponse("Please use '/admin' to create pricing configurations and '/pricing/calculate-pricing/distance/time/waiting_time' to test price calculation API")