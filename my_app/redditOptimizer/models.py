from django.db import models

# Create your models here.
class InputBox(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class OutputBox(models.Model):
    subreddit1 = models.CharField(max_length=100)
    subreddit2 = models.CharField(max_length=100)
    subreddit3 = models.CharField(max_length=100)
    subreddit4 = models.CharField(max_length=100)
    subreddit5 = models.CharField(max_length=100)


    def __str__(self):
        """A string representation of the model."""
        return self.title
