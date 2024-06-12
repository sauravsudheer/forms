from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('success/<int:registration_number>/', views.success, name='success'),
    path('userdisplay/', views.userdisplay, name='register_and_display'),
    path('generate-pdf/<int:registration_number>/', views.generate_pdf, name='generate_pdf'),
]