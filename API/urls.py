from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes),
    ##############
    path("leden/", views.getLeden),
    path("leden/<str:pk>", views.getLid),
    #########
    path("documents/", views.getDocuments),
    path("boekstuken/", views.boekstuken),
    path("decla/", views.getDeclas),
    path("decla/<str:decla_id>", views.getDecla),
    path("add_document/", views.add_Document),
    ####################
    path("events/", views.getEvents),
    path("events/<str:pk>", views.getEvent),
    # path("create-event/", views.addEvents),
    # path("edit-event/<str:pk>", views.editEvent),
    # path("delete-event/<str:pk>", views.deleteEvent),
    # ##################
    path("dsani/", views.Dsani),
    path("dsani/pages/<int:pagenum>", views.Dsani),
    path("dsani/<str:nievent_id>", views.getDsani),
    # path("edit-dsani/<str:nievent_id>", views.editDsani),
    # path("delete-dsani/<str:nievent_id>", views.deleteDsani),
    ###
    path("users/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    ####
]
