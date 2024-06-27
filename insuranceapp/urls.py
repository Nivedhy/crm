from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_agent/', views.add_agent, name='add_agent'),  
    path('edit_agent/', views.edit_agent, name='edit_agent'),
    path('delete_agent/', views.delete_agent, name='delete_agent'),
    path('add_policy/', views.add_policy, name='add_policy'), 
    path('edit_policy//', views.edit_policy, name='edit_policy'),
    path('delete_policy/', views.delete_policy, name='delete_policy'),
    path('view_agent/', views.view_agent, name='view_agent'),  
    path('view_agent_locations/', views.view_agent_locations, name='view_agent_locations'),  
    path('agent/', views.agent_dashboard, name='agent_dashboard'),  
    path('add_customer/', views.add_customer, name='add_customer'),  
    path('view_customer/', views.view_customer, name='view_customer'),  
    path('edit_customer/', views.edit_customer, name='edit_customer'),  
    path('delete_customer/', views.delete_customer, name='delete_customer'),  
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'), 
    path('campaign/',views.campaign,name='campaign'),
    path('campaign_meet/',views.campaign_meet,name='campaign_meet'),
]
