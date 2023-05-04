from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('loginhw/', views.loginhw, name='loginhw'),
    path('autenticar/', views.autenticar, name='autenticar'),  
    path('', views.dashboardhw, name='dashboardhw'), 
    path('dashboardhws', views.dashboardhws, name='dashboardhws'), 
    path('smsEmail/', views.smsEmail, name='smsEmail'),  
    path('help/', views.help, name='help'), 
    path('icareplus/', views.icareplus, name='icareplus'), 
    path('netcare/', views.netcare, name='netcare'), 
    path('onebox/', views.onebox, name='onebox'), 
    path('profile/', views.profile, name='profile'), 
    path('vpnaccess/', views.vpnaccess, name='vpnaccess'), 
]