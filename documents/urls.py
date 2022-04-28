from django.urls import path
from . import views

urlpatterns = [

    path('add-document/', views.addDocument, name='add-document'),
    path('edit-document/<str:pk>', views.editDocument, name='edit-document'),
    path('delete-document/<str:pk>', views.deleteDocument, name='delete-document'),

    path('document/<str:pk>', views.showDocument, name='document'),
    path('documents/', views.showDocuments, name='documents'),
    path('documents/<int:year>', views.showDocumentsPerYear, name='documentsPerYear'),
]