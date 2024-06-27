from django.shortcuts import render




def home(request):
    return render(request, 'home.html')

def agent_dashboard(request):
    return render(request, 'agent_dashboard.html')

def view_agent_locations(request):
    agents = [
        {
            'name': 'NIvedhya',
            'location_history': {
                '2024-06-01': [
                    {'time': '10:00 AM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'panoor Kannur, KL, IND'},
                    {'time': '02:00 PM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'kavadathur Thalassery, CA, USA'},
                    
                ],
                '2024-06-02': [
                    {'time': '09:00 AM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'valayam Kozhikode, KL, IND'},
                    {'time': '03:00 PM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'irighanoor Kozhikode, KL, IND'},
                    
                ],
            
            }
        },
        {
            'name': 'Rajeevan',
            'location_history': {
                '2024-06-01': [
                    {'time': '11:00 AM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'Batheri Wayanad, KL, IND'},
                    {'time': '01:00 PM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'East Wayanad, KL, IND'},
                
                ],
                '2024-06-02': [
                    {'time': '10:00 AM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'Perambra Kozhicode, KL, IND'},
                    {'time': '04:00 PM', 'latitude': 34.0522, 'longitude': -118.2437, 'place': 'Mokeri Kozhicode, KL, IND'},
                    
                ],
                
            }
        }
        
    ]

    return render(request, 'view_agent_locations.html', {'agents': agents})



def view_agent(request):
    return render(request, 'view_agent.html')

def add_customer(request):
   return render(request, 'add_customer.html')

def edit_customer(request):
   return render(request, 'edit_customer.html')

def delete_customer(request):
   return render(request,'delete_customer.html')

def view_customer(request):
   return render(request, 'view_customer.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def add_agent(request):
    return render(request, 'add_agent.html')

def edit_agent(request):
    return render(request, 'edit_agent.html')

def delete_agent(request):
    return render(request, 'delete_agent.html')

def add_policy(request):
    return render(request, 'add_policy.html')

def edit_policy(request):
    return render(request, 'edit_policy.html')

def delete_policy(request):
    
    return render(request, 'delete_policy.html')


def campaign(request):
    return render(request,'campaign.html')

def campaign_meet(request):
    return render(request,'campaign_meet.html')



