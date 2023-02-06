from django import forms

from detection.models import CTScan
class CTScanForm(forms.ModelForm):
    class Meta:
        model = CTScan
        fields = ['patient_name', 'ct_scan']