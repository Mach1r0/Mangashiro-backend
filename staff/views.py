from rest_framework import viewsets
from staff.models import Staff
from staff.serializer import StaffSerializer 

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
