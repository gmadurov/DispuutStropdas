from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('register/', views.registerUser, name='register'),

    path('', views.lids, name='lids'),
    path('lid/<str:pk>', views.userLid, name='user-lid'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),


    # path('document/<str:pk>', views.showDoc, name='document'),

]