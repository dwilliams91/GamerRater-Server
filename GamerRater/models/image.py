from django.db import models

class Images(models.model):
    game=models.ForeignKey("Games", verbose_name=_(""), on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", verbose_name=_(""), on_delete=models.CASCADE)
    image=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)