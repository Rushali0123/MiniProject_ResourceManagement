from django.shortcuts import render, redirect
from resource.models import Resource
from assign.models import addAssigned, addBillable
from django.contrib.auth.decorators import login_required

# Create your views here.

def addres(request):
    if request.method == "POST":
        resource_name = request.POST["Resource_name"]
        resource_desc = request.POST["desc"]
        if resource_name == "" or resource_desc == "":
            pass
        else:
            res = Resource.objects.create(name = resource_name, desc = resource_desc)
            res.save()

            return redirect("home")
        
def res(request):
    Course = Resource.objects.all()
    assigned = addAssigned.objects.all()
    billable = addBillable.objects.all()
    data = {
        'data':Course,
        'assigned': assigned,
        'billable': billable    
    }

    return render(request, 'home.html', data)

