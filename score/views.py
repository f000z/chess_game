from rest_framework import generics
from .models import Score
from .serializers import ScoreCreateSerializer, ScoreListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ScoreCreateListView(generics.ListCreateAPIView):
    queryset = Score.objects.select_related('game','player').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game','player','result']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ScoreCreateSerializer
        return ScoreListSerializer

class ScoreDetailView(generics.RetrieveDestroyAPIView):
    queryset = Score.objects.select_related('game','player').all()
    serializer_class = ScoreListSerializer
