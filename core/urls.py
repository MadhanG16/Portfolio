"""
URL patterns for the core portfolio app.
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact'),
]
