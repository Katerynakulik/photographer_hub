from django.urls import path
from . import views

urlpatterns = [
    path('create-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('wh/', views.stripe_webhook, name='stripe_webhook'),
]