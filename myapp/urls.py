from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),
]