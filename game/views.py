from rest_framework import generics, status
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

class GameCreateListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.has_scores():
            return Response({"error":"Cannot delete game with existing scores. Tournament has active games."}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)
