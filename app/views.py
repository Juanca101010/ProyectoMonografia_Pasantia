from django.shortcuts import render
from django.http import HttpResponse

def dashboardhw(request):

    return render(request, 'app/dashboardhw.html')
def smsEmail(request):

    return render(request, 'app/smsEmail.html')
def loginhw(request):

    return render(request, 'app/loginhw.html')
def help(request):

    return render(request, 'app/help.html')
def icareplus(request):

    return render(request, 'app/icareplus.html')
def netcare(request):

    return render(request, 'app/netcare.html')
def onebox(request):

    return render(request, 'app/onebox.html')
def profile(request):

    return render(request, 'app/profile.html')
def vpnaccess(request):

    return render(request, 'app/vpnaccess.html')