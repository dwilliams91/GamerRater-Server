from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamerraterapi.models import Games, Gamers, Ratings

class All_Ratings(ViewSet):
    def list(self, request):
        ratings=Ratings.objects.all()
        # gamer = Gamers.objects.get(user=request.auth.user)

        # game=Games.objects.get(id=ratings.game)

        serializer=RatingSerializer(ratings, many=True, context={'request': request})


        return Response(serializer.data)



# class EventUserSerializer(serializers.ModelSerializer):
#     """JSON serializer for event scheduler's related Django user"""
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Games
        fields=("id", "title")

class RatingSerializer(serializers.ModelSerializer):
    game=GameSerializer(many=False)
    class Meta:
        model= Ratings
        fields=("id", "rating", "gamer", "game")