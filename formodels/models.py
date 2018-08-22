from django.db import models

class airjordan(models.Model):
    jordantype=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    def __str__(self):
        return self.jordantype
    def __str__(self):
        return self.color
