from rest_framework import permissions
from rest_framework import viewsets

from backend.models import Attack, Report, Village
from backend.serializers import AttackCreateSerializer, AttackSerializer, VillageSerializer, ReportSerializer, \
    ReportCreteSerializer, VillageCreateSerializer


class AttackViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return AttackCreateSerializer

        return AttackSerializer


class VillageViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return VillageCreateSerializer

        return VillageSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReportCreteSerializer

        return ReportSerializer
