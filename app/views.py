from django.shortcuts import render
from django.http import HttpResponse

def dashboardhw(request):

    return render(request, 'app/dashboardhw.html')
def smsEmail(request):

    return render(request, 'app/smsEmail.html')
def loginhw(request):

    return render(request, 'app/loginhw.html')