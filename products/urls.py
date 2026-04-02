from django.urls import path  # <--- This was the missing piece!
from . import views

urlpatterns = [
    path('all/', views.all_products, name='all_products'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add-photo/', views.add_product, name='add_product'),
    path('dashboard/add-session/', views.add_session, name='add_session'),
    path('photoshoot/<int:pk>/', views.photoshoot_detail, name='photoshoot_detail'),
]