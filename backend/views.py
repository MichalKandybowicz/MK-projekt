from rest_framework import permissions
from rest_framework import viewsets

from backend.models import Attack
from backend.serializers import AttackSerializer


class AttackViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    permission_classes = [permissions.AllowAny]
