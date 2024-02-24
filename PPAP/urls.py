"""
URL configuration for PPAP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ppap_app.views import home_page, ongoing_page, upcoming_page, game_page, player_info_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_page, name='home'),
    path('ongoing/', ongoing_page, name='ongoing'),
    path('upcoming/', upcoming_page, name='upcoming'),
    path('game/<int:id>', game_page, name='game_page'),
    path('player_info/<int:id>', player_info_page, name='player_info'),

    ]