from rest_framework import viewsets, permissions

from API.serializers import ApplicationSerializer
from Applications import models


# Create your views here.
class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = models.Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

