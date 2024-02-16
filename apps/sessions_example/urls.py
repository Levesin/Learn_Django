from django.urls import path

from . import views

app_name = 'sessions'

urlpatterns = [
    path('', views.SessionExampleView.as_view(), name='index'),
]
