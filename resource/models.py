from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name
    

