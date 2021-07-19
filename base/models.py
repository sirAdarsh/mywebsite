from django.db import models

# Create your models here.
class Queries(models.Model):
    Name = models.CharField(max_length=30)
    Description = models.TextField(max_length=400)
    EmailID = models.CharField(max_length=50)

    def __str__(self):
        return f"Query by: {self.Name}"