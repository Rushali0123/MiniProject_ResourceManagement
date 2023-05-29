from django.shortcuts import render, redirect,get_object_or_404
from .models import Assigned, addAssigned, addBillable
from resource.models import Resource


def _Assigned_id(request):
    assign = request.session.session_key
    if not assign:
        assign = request.session.create()
    return assign


def Assigned1(request, id):
    resource = Resource.objects.get(id=id)
    try:
        assign_re = Assigned.objects.get(resource_id=_Assigned_id(request))
    except Assigned.DoesNotExist:
        assign_re= Assigned.objects.create(resource_id=_Assigned_id(request))
    assign_re.save()
    try:
        assign_resource_billed = addBillable.objects.filter(resource=resource)
       
        if assign_resource_billed.exists():
            
            return redirect('home')
        assign_resource = addAssigned.objects.get(resource=resource)
        assign_resource.save()
    except addAssigned.DoesNotExist:
        assign_resource = addAssigned.objects.create(
            resource=resource,
            assigned=assign_re,
        )
        
        assign_resource.save()
    return redirect('home')
    

def AssignedRemove(request,id):
    assign = Assigned.objects.get(resource_id=_Assigned_id(request))
    resource = get_object_or_404(Resource, id=id)
    assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
    assigned_resource.delete()
   
    return redirect('home')

def billable(request, id):
  
    resource = Resource.objects.get(id=id)
    try:
        assign_resource = addAssigned.objects.filter(resource=resource)
        if assign_resource.exists():
            assign_resource_bill = addBillable.objects.create(
            resource=resource,
            )
            assign_resource_bill.save()
            
            assign = Assigned.objects.get(resource_id=_Assigned_id(request))
            resource = get_object_or_404(Resource, id=id)
            assigned_resource = addAssigned.objects.get(resource=resource, assigned=assign)
            assigned_resource.delete()
    except addAssigned.DoesNotExist:
        pass
    return redirect('home')

    

def billableRemove(request,id):
    resource = get_object_or_404(Resource, id=id)
    assigned_resource = addBillable.objects.get(resource=resource)
    assigned_resource.delete()
    
    return redirect('home')
