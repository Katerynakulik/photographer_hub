from django.urls import path
from . import views

urlpatterns = [
    path('delete-session/<int:pk>/', views.delete_session, name='delete_session'),]
