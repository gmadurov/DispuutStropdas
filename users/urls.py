from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    # path("load-data/", views.loadDATA, name="loadData"),
    # path('register/', views.registerUser, name='register'),
    path("", views.home, name="home"),
    path("mainPage", views.fakePage, name="fakePage"),
    path("leden", views.leden, name="leden"),
    path("lid/<str:pk>", views.userLid, name="user-lid"),
    path("account/", views.userAccount, name="account"),
    path("edit-account/", views.editAccount, name="edit-account"),
    # path('document/<str:pk>', views.showDoc, name='document'),
]
