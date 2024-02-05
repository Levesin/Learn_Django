from django.urls import path
from apps.contacts import views

app_name = 'contacts'

urlpatterns = [
    path('contacts_list/', views.list_contacts, name='contacts_list')
]
