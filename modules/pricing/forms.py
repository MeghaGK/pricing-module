from django import forms
from .models import PricingConfiguration

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = ['name', 'base_distance', 'dbp', 'dap', 'tmf', 'base_wc','wc', 'is_active']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
