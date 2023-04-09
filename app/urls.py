from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('', views.dashboardhw, name='dashboardhw'), 
    path('smsEmail', views.smsEmail, name='smsEmail'), 
    path('loginhw', views.loginhw, name='loginhw'), 
]