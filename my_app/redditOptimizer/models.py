from django.db import models

# Create your models here.
class InputBox(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class OutputBox(models.Model):
    subred = models.CharField(max_length=100)
    link = models.CharField(max_length=100)


    def __str__(self):
        """A string representation of the model."""
        return self.title
