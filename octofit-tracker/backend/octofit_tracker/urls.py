from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Welcome to Octofit Tracker Backend</h1><p>API endpoints are available at /api/</p>')
"""octofit_tracker URL Configuration

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

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from octofit_tracker.models import Activity, User, Team, Leaderboard, Workout

def api_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    return JsonResponse({'api_base_url': f'https://{codespace_name}-8000.app.github.dev/api/'})

def activities_list(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    data = list(Activity.objects.values())
    return JsonResponse({'url': f'https://{codespace_name}-8000.app.github.dev/api/activities/', 'data': data})

def users_list(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    data = list(User.objects.values())
    return JsonResponse({'url': f'https://{codespace_name}-8000.app.github.dev/api/users/', 'data': data})

def teams_list(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    data = list(Team.objects.values())
    return JsonResponse({'url': f'https://{codespace_name}-8000.app.github.dev/api/teams/', 'data': data})

def leaderboard_list(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    data = list(Leaderboard.objects.values())
    return JsonResponse({'url': f'https://{codespace_name}-8000.app.github.dev/api/leaderboard/', 'data': data})

def workouts_list(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    data = list(Workout.objects.values())
    return JsonResponse({'url': f'https://{codespace_name}-8000.app.github.dev/api/workouts/', 'data': data})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', api_base_url),
    path('api/activities/', activities_list),
    path('api/users/', users_list),
    path('api/teams/', teams_list),
    path('api/leaderboard/', leaderboard_list),
    path('api/workouts/', workouts_list),
]
