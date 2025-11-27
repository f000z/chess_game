from django.urls import path
from .views import ScoreCreateListView, ScoreDetailView

urlpatterns = [
    path('', ScoreCreateListView.as_view(), name='scores-list'),
    path('<int:pk>/', ScoreDetailView.as_view(), name='score-detail'),
]
