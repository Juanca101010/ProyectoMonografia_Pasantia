from django.urls import path 
from . import views 
from app.views import RestorePassView

app_name = 'app' 
urlpatterns = [
    path('', views.loginhw, name='loginhw'),
    path('ADMIN/', views.ADMIN, name='ADMIN'),
    path('restorepass/', RestorePassView.as_view(), name='restorepass'),
    path('autenticar/', views.autenticar, name='autenticar'),  
    path('dashboardhw', views.dashboardhw, name='dashboardhw'), 
    path('dashboardhws', views.dashboardhws, name='dashboardhws'), 
    path('smsEmail/', views.smsEmail, name='smsEmail'),  
    path('help/', views.help, name='help'), 
    path('icareplus/', views.icareplus, name='icareplus'), 
    path('netcare/', views.netcare, name='netcare'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('onebox/', views.onebox, name='onebox'), 
    path('profile/', views.profile, name='profile'), 
    path('vpnaccess/', views.vpnaccess, name='vpnaccess'),
    path('ejecutartarea/', views.ejecutartarea, name='ejecutartarea'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit_task2/<int:task_id>/', views.edit_task2, name='edit_task2'),
    path('edit_task3/<int:task_id>/', views.edit_task3, name='edit_task3'),
    path('edit_task4/<int:task_id>/', views.edit_task4, name='edit_task4'),
    path('edit_task5/<int:task_id>/', views.edit_task5, name='edit_task5'),
    path('edit_task6/<int:task_id>/', views.edit_task6, name='edit_task6'),
]