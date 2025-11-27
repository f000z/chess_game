from rest_framework import serializers
from .models import Player
from django.db.models import Count, Q

class PlayerListSerializer(serializers.ModelSerializer):
    total_games = serializers.IntegerField(read_only=True)
    wins = serializers.IntegerField(read_only=True)
    draws = serializers.IntegerField(read_only=True)
    losses = serializers.IntegerField(read_only=True)

    class Meta:
        model = Player
        fields = ['id','nickname','country','rating','total_games','wins','draws','losses','created_at']

class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','nickname','country','rating','created_at']
        read_only_fields = ('id','rating','created_at')
