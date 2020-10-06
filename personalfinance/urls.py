from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='pf_dashboard')
]
