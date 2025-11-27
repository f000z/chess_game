from rest_framework import generics
from django.db.models import Count, Q
from .models import Player
from .serializers import PlayerListSerializer, PlayerCreateSerializer


class PlayerListCreateView(generics.ListCreateAPIView):
    queryset = Player.objects.all().annotate(
        total_games=Count('scores'),
        wins=Count('scores', filter=Q(scores__result='win')),
        draws=Count('scores', filter=Q(scores__result='draw')),
        losses=Count('scores', filter=Q(scores__result='loss')),
    )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PlayerCreateSerializer
        return PlayerListSerializer


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all().annotate(
        total_games=Count('scores'),
        wins=Count('scores', filter=Q(scores__result='win')),
        draws=Count('scores', filter=Q(scores__result='draw')),
        losses=Count('scores', filter=Q(scores__result='loss')),
    )
    serializer_class = PlayerListSerializer
