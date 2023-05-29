from django.db import models
from resource.models import Resource
class Assigned(models.Model):
    resource_id = models.CharField( max_length=50)
    assign_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.resource_id
class addAssigned(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    assigned = models.ForeignKey(Assigned, on_delete=models.CASCADE, null=True) 


class addBillable(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE) 

   