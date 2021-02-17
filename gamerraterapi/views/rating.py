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
    def retrieve(self, request, pk=None):
        
        try:
            rating=Ratings.objects.get(pk=pk)
            serializer=RatingSerializer(rating, context={'request':request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        ratings=Ratings.objects.all()
        # gamer = Gamers.objects.get(user=request.auth.user)

        # game=Games.objects.get(id=ratings.game)

        serializer=RatingSerializer(ratings, many=True, context={'request': request})


        return Response(serializer.data)


    def create(self, request):
       

        # Uses the token passed in the `Authorization` header
        gamer = Gamers.objects.get(user=request.auth.user)
        game = Games.objects.get(pk=request.data["gameId"])
        
        rating = Ratings()
        rating.gamer = gamer
        rating.rating=request.data["rating"]
        rating.game=game

        
        try:
            rating.save()
            serializer = RatingSerializer(rating, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
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
        