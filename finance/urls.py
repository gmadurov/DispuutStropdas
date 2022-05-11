from django.urls import path
from . import views

urlpatterns = [
    path('decla/', views.fileDecla, name = 'fileDecla'),
    path('declas-verwerken/', views.verwerkenDecla, name = 'verwerkenDecla'),
    path('edit-decla/<str:pk>/', views.editDecla, name = 'editDecla'),
    path('delete-decla/<str:pk>/', views.deleteDecla, name = 'deleteDecla'),
    path('show-decla/<str:pk>/', views.showDecla, name = 'showDecla'),
    
]
