from django.shortcuts import render

# Create your views here.

def feeCollection(request):
    variable = {"First": 500,"Second":1500,"Final":2000}
    return render(request,"finance/feeCollection.html",variable)

def feeDuesReport(request):
    return render(request,"finance/feeDuesReport.html")

def feeCollectionReport(request):
    return render(request,"finance/feeCollectionReport.html")