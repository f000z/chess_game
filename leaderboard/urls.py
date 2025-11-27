from django.urls import path
from .views import GameLeaderboardView, TopPlayersLeaderboardView, GlobalLeaderboardView

urlpatterns = [
    path('game/', GameLeaderboardView.as_view(), name='game-leaderboard'),
    path('game/top/', TopPlayersLeaderboardView.as_view(), name='top-players-leaderboard'),
    path('global/', GlobalLeaderboardView.as_view(), name='global-leaderboard'),
]
