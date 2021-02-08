import django.db from models

class GamerCategories(models.Model):

    game= models.ForeignKey("Games", verbose_name=_(""), on_delete=models.CASCADE)(User, on_delete=models.CASCADE)
    category=models.ForeignKey("Categories", verbose_name=_(""), on_delete=models.CASCADE)
    gamer=models.ForeignKey("Gamers", verbose_name=_(""), on_delete=models.CASCADE)