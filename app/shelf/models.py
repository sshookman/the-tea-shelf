from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=100) # Unique Tea Name
    variety = models.CharField(max_length=100) # Green, Oolong, Black, White, Fruit, Herbal, etc.
    source = models.CharField(max_length=100) # The Source from which the Tea was Procured
    steep_time = models.IntegerField(default=120) # Time in Seconds
    steep_temp = models.IntegerField(default=112) # Temp in Fahrenheit
    tsp_per_cup = models.FloatField(default=1) # Teaspoons Per Cup

    def __str__(str):
        return f"{self.name} {self.variety} Tea from {source}"
