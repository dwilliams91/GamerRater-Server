import django.db from models

class Ratings(models.Model):
    game=models.ForeignKey("Games", on_delete=models.CASCADE)
    rating=models.IntegerField()
    gamer=models.ForeignKey("Gamers", on_delete=models.CASCADE)