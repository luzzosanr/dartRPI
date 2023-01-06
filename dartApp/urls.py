"""dartApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from memory.api import add_shot, start_game, get_game_types, new_game_type, current_game, last_shot, fake_shot
from memory import consumers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_shot/', add_shot),
    path('start_game/', start_game),
    path('get_game_types/', get_game_types),
    path('new_game_type/', new_game_type),
    path('current_game/', current_game),
    path('last_shot/', last_shot),
    path('fake_shot/', fake_shot),
]
