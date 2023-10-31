"""registration URL Configuration

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
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcameraLocation/',views.addcameraLocation, name='addcameraLocation'),
    path('',views.HomePage,name='login'),
    path('forest_department_login/',views.SignupPage,name='forest_department_login'),
    path('user_home/',views.user_home, name = 'user_home'),
    path('forest_home/',views.forest_home, name = 'forest_home'),
    path('get-markers/',views.get_markers,name='user_map'),
    path('get-markers/',views.forest_map,name='forest_map'),
    path('report/',views.report,name='report'),
    path('suggest/',views.suggestions,name='suggest'),
    ]
