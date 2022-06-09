"""comgeld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin1"),
    # path('links/', include('links.urls')),
    path("", include("users.urls")),
    path("", include("agenda.urls")),
    path("", include("documents.urls")),
    path("", include("finance.urls")),
    path("api/", include("API.urls")),
    # path('accounts/', include('allauth.urls')),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="password/reset-password.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password/reset-password-sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password/reset.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password/reset-password-complete.html"
        ),
        name="password_reset_complete",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from .settings import path as pa

if os.getcwd() == pa:
    from environment.start_up_db import *

    urlpatterns.append(path("start_events/", startEVENTS, name = 'start_event'))
    urlpatterns.append(path("start_leden/", startLEDEN, name = 'start_leden'))
    urlpatterns.append(path("start_decla/", startDECLA, name = 'start_decla'))
    urlpatterns.append(path("start_all/", start_all, name = 'start_all'))
    urlpatterns.append(path("delete_event/", deleteEVENTS, name = 'delete_event'))
    urlpatterns.append(path("delete_leden/", deleteLEDEN, name = 'delete_leden'))
    urlpatterns.append(path("delete_decla/", deleteDECLA, name = 'delete_decla'))


# 1 - User submits email for reset              //PasswordResetView.as_view()           //name="reset_password"
# 2 - Email sent message                        //PasswordResetDoneView.as_view()        //name="passsword_reset_done"
# 3 - Email with link and reset instructions    //PasswordResetConfirmView()            //name="password_reset_confirm"
# 4 - Password successfully reset message       //PasswordResetCompleteView.as_view()   //name="password_reset_complete
