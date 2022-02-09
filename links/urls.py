from . import views
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name='agenda')
]