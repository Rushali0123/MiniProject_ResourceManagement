from django.urls import path
from .views import *
urlpatterns = [
    path('assigned/<int:id>', Assigned1, name="Assigned"),
    path('billable/<int:id>', billable, name="billable"),
    path('assigned-remove/<int:id>', AssignedRemove, name="AssignedRemove"),
    path('billable-remove/<int:id>', billableRemove, name="billableRemove"),
]
