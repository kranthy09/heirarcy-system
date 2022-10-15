from django.db import models

# Create your models here.
class Level(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return str(self.id) + "  |  " + self.name

class SubLevel(models.Model):
    name = models.CharField(unique=True, max_length=255)
    parent = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='sublevels')

    def __str__(self) -> str:
        return str(self.id) + "  |  " + self.name
