from django.db import models

class Ratings(models.Model):
    game=models.ForeignKey("Games", on_delete=models.CASCADE, related_name="ratings")
    rating=models.IntegerField()
    gamer=models.ForeignKey("Gamers", on_delete=models.CASCADE)