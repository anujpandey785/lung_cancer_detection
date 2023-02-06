from django.db import models

class CTScan(models.Model):
    patient_name = models.CharField(max_length=100)
    ct_scan = models.ImageField(upload_to='ct_scans/')
    result = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.patient_name