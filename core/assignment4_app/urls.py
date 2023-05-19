from assignment4_app import views
from django.urls import path, include

urlpatterns = [
    path('product/', views.home, name='product'),
]