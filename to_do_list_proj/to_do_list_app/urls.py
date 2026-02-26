from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_to, name='add_to'),
    path('edit/<int:pk>/', views.edit_to, name='edit_to'),
    path('delete/<int:pk>/', views.delete_to, name='delete_to'),
    path('details/<str:pk>/', views.details_to, name='details_to'),
    path('search/', views.search_to, name='search_to'),
]