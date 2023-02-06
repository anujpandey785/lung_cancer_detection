from django.shortcuts import render, redirect
from lung_cancer_detection.forms import CTScanForm
#from forms import CTScanForm
from .models import CTScan


def index(request):
    if request.method == 'POST':
        form = CTScanForm(request.POST, request.FILES)
        if form.is_valid():
            ct_scan = form.save()
            
            # Pass the CT scan to the machine learning model to get the result
            result = predict_result(ct_scan.ct_scan.path)
            
            # Save the result in the database
            ct_scan.result = result
            ct_scan.save()
            
            return redirect('result', pk=ct_scan.pk)
    else:
        form = CTScanForm()
    return render(request, 'detection/index.html', {'form': form})

def result(request, pk):
    ct_scan = CTScan.objects.get(pk=pk)
    return render(request, 'detection/result.html', {'ct_scan': ct_scan})

def predict_result(ct_scan_path):

    

    return result