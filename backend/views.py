from rest_framework import permissions
from rest_framework import viewsets

from backend.models import Attack, VillageDetailInformation
from backend.serializers import AttackSerializer, VillageDetailInformationSerializer


class AttackViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    permission_classes = [permissions.AllowAny]


class VillageViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = VillageDetailInformation.objects.all()
    serializer_class = VillageDetailInformationSerializer
    permission_classes = [permissions.AllowAny]
