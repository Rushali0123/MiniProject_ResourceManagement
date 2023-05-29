from django.urls import path
from .views import *
urlpatterns = [
    path('resources', res, name="Resource"),
    path('addResource', addres, name = "addResource")
]
