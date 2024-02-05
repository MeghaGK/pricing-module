from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PricingConfiguration(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dbp = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="DBP")
    base_distance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Base Distance")
    dap = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="DAP")
    tmf = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="TMF")
    base_wc = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Base Waiting Time")
    wc = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="WC")
    is_active = models.BooleanField(default=True)
    last_modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    last_modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            self.last_modified_by = user
        self.last_modified_at = timezone.now()
        super().save(*args, **kwargs)
