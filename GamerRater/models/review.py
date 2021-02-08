from django.db import models

class Reviews(models.Model):
    game=models.ForeignKey("Games", verbose_name=_(""), on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", verbose_name=_(""), on_delete=models.CASCADE)
    review=models.CharField(_(""), max_length=250)