from django.urls import path
from .views import GameCreateListView, GameDetailView

urlpatterns = [
    path('', GameCreateListView.as_view(), name='games-list-create'),
    path('<int:pk>/', GameDetailView.as_view(), name='games-detail'),
]
