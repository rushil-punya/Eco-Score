"""trailAssess URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from login import views as v
from ecoscore import views as ves
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', v.login_view, name = "login"),
    path('', views.homepage, name = "home"),
    path('user/', views.homepageLogin, name = "logged"),
    path('ecoscore/', ves.charts, name="ecoButton"),
    path('calculate/', ves.calculate, name = "calculate"),
    #this url takes care of the redirects when users click on a button in the
    #'ecoscore' app. These redirects are important because it lets the system know
    #that the user's eco score needs to be updated later
    url(r'^(?P<slug>[\w-]+)/$', ves.select, name="select"),
    path('', include("login.urls")),
    path('', include("django.contrib.auth.urls")),

    ]
app_name = "trailAssess"

