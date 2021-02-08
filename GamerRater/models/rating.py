import django.db from models

class Ratings(models.Model):
    game=models.ForeignKey("Games", verbose_name=_(""), on_delete=models.CASCADE)
    rating=models.IntegerField(_(""))
    gamer=models.ForeignKey("Gamers", verbose_name=_(""), on_delete=models.CASCADE)