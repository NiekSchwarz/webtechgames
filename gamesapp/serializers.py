from rest_framework import serializers
from .models import Game, HighScore


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_id', 'name', 'description', 'genre', 'date_added')


class HighScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighScore
        fields = ('id', 'game_id', 'user_id', 'score', 'date_added')
