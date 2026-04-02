from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_products, name='all_products'),
    path('dashboard/', views.photographer_dashboard, name='dashboard'),
    # Mentor Note: CRUD paths will be added here once forms are ready
]