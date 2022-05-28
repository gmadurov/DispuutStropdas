from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name = 'agenda'),
    path('afgelopen-agenda/', views.afgelopenAgenda, name = 'afgelopenAgenda'),
    path('dsani/', views.dsani, name = 'DSANI'),

    path('tryout/', views.try_out, name = 'try_out'),
    path('add-event/', views.create_event, name = 'createEvent'),
    path('edit-event/<str:pk>', views.edit_event, name = 'editEvent'),
    path('delete-event/<str:pk>', views.delete_event, name = 'deleteEvent'),

    path('edit-dsani/<str:pk>', views.edit_dsani, name = 'edit-dsani')
]