from django.db import models

class Reviews(models.Model):
    game=models.ForeignKey("Games",  on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", on_delete=models.CASCADE)
    review=models.CharField(max_length=250)