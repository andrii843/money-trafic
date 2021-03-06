from django.db import models
from users.models import User
from saves.models import Save
from categories.models import Category


class Outcome(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    summa = models.DecimalField(max_digits=15, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    fsave = models.ForeignKey(Save, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'outcomes'
