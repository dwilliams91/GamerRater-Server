from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Games, Gamers

class All_Games(ViewSet):

    
    def retrieve(self, request, pk=None):
        try:

            game=Games.objects.get(pk=pk)
            serializers=GameSerializer(game, context={'request':request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        print("does this hit?")
        games=Games.objects.all()

        serializer=GameSerializer(games, many=True, context={'request':request})
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Games
        fields=("id", "title", "year", "number_of_players", "age_recommendation", "play_time")
