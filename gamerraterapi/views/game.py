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
            serializer=GameSerializer(game, context={'request':request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        games=Games.objects.all()

        serializer=GameSerializer(games, many=True, context={'request':request})
        return Response(serializer.data)

    def create(self, request):
        gamer=Gamers.objects.get(user=request.auth.user)
        game=Games()
        game.title=request.data['title']
        game.description=request.data['description']
        game.year=request.data['year']
        game.number_of_players=request.data['numberOfPlayers']
        game.play_time=request.data['playTime']
        game.age_recommendation=request.data['ageRecommendation']
        game.gamer= gamer


        try:
            game.save()
            serializer=GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        print("hello")
        try:
            game=Games.objects.get(pk=pk)
            game.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Games
        fields=("id", "title", "gamer", "year", "description", "number_of_players", "age_recommendation", "play_time")
