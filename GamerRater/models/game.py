import django.db from models

class Games(models.Model):

    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    gamer=models.ForeignKey("Gamers", verbose_name=_(""), on_delete=models.CASCADE)
    year=models.IntegerField(_(""))
    number_of_players=models.IntegerField(_(""))
    play_time= models.IntegerField(_(""))
    age_recommendation= models.IntegerField(_(""))
