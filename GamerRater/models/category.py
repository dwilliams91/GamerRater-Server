from django.db import models

class Categories(models.Model):
    category=models.CharField(_(""), max_length=50)