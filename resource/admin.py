from django.contrib import admin
from .models import Resource

# Register your models here.
class  resourceAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
    
admin.site.register(Resource,resourceAdmin)