from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/game/', include('game.urls')),
    path('api/players/', include('players.urls')),
    path('api/scores/', include('score.urls')),
    path('api/leaderboard/', include('leaderboard.urls')),
]
