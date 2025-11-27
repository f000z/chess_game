from rest_framework import serializers
from .models import Score
from game.serializers import GameSerializer
from players.serializers import PlayerListSerializer
from game.models import Game
from players.models import Player

class ScoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id','game','player','result','opponent_name','points','created_at']
        read_only_fields = ('id','points','created_at')

    def validate_result(self, value):
        if value not in ['win','draw','loss']:
            raise serializers.ValidationError("Result must be 'win','draw' or 'loss'.")
        return value

class ScoreListSerializer(serializers.ModelSerializer):
    game = serializers.SerializerMethodField()
    player = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ['id','game','player','result','points','opponent_name','created_at']

    def get_game(self, obj):
        return {'id': obj.game.id, 'title': obj.game.title}

    def get_player(self, obj):
        return {'id': obj.player.id, 'nickname': obj.player.nickname}
