from django.db import models

class GamerCategories(models.Model):

    game= models.ForeignKey("Games", on_delete=models.CASCADE)
    category=models.ForeignKey("Categories",  on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", on_delete=models.CASCADE)