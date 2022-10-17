from pyexpat import model
from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(unique=True, max_length=50)
    level = models.IntegerField()

    def __str__(self) -> str:
        return self.name + "  |  " + "level:" + str(self.level)

class Child(models.Model):
    name = models.CharField(unique=True, max_length=50)
    level = models.IntegerField(null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="childs")

    def __str__(self) -> str:
        return self.name + "  |  " + "level:" + str(self.level)
