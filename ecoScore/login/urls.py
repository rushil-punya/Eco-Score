from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
urlpatterns = [
    path('login/logout/', views.logout_view, name = "logout"),
    path('login/createaccount/', views.register, name = "createaccount"),
    ]
app_name = 'login'
