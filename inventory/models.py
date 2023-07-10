from django.db import models
""" from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles """

categories = [('HARDWARE','Hardware'),('ART SUPPLIES','Art Supplies'),('OTHER','Other')]
class Item(models.Model):
    updated = models.DateTimeField(auto_now=True, editable=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=categories, default='')

    def __str__(self):
        return self.name



