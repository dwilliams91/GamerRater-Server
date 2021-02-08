from django.db import models

class Images(models.model):
    game=models.ForeignKey("Games", on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", on_delete=models.CASCADE)
    image=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)