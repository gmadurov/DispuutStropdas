from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('leden/', views.getLeden),
    path('lid/<str:pk>', views.getLid),
    path('documents/', views.getDocuments),
    path('decla/', views.makeDecla),
    path('decla/<str:decla_id>', views.getDecla),
    path('add_document/', views.add_Document),
    path('Events/', views.getEvents),
    path('NIEvents/', views.getNIEvents),
    path('NI_events/<str:nievent_id>/', views.getNIEvent),
    path('NI_events/<str:lid_id>/<str:nievent_id>/', views.NI_points),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
