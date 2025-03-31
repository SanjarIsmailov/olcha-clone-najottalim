from django.urls import path
from . import views  # Ensure you have views imported

urlpatterns = [
    path('', views.home, name='home'),  # Example home view
    # Add other paths here
]
