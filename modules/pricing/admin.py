from django.contrib import admin
from .models import PricingConfiguration
from .forms import PricingConfigurationForm

class PricingConfigurationAdmin(admin.ModelAdmin):
    form = PricingConfigurationForm
    list_display = ['name', 'dbp', 'dap', 'tmf', 'wc', 'is_active']

admin.site.register(PricingConfiguration, PricingConfigurationAdmin)
