"""MedQuestions URL Configuration
# urls.py
# Created by Egor Matveev
# 16.05.2021
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
from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results', views.results),
    path('plot', views.plot),
    path('temperament_result', views.temperament_result),
    path('about_temperament', views.about_temperament),
    path('about_role', views.about_role),
    path('role_test', views.role_test),
    path('end', views.end),
    path('temperament_test', views.temperament_test),
    path('', views.main)
]
