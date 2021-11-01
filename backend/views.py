from rest_framework import mixins
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet

from backend.models import Attack, Report, Village
from backend.serializers import AttackCreateSerializer, AttackSerializer, VillageSerializer, ReportSerializer, \
    ReportCreteSerializer, VillageCreateSerializer


class CustomModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class AttackViewSet(CustomModelViewSet):
    """
    """
    queryset = Attack.objects.all()
    serializer_class = AttackSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return AttackCreateSerializer

        return AttackSerializer


class VillageViewSet(CustomModelViewSet):
    """
    """
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return VillageCreateSerializer

        return VillageSerializer


class ReportViewSet(CustomModelViewSet):
    """
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReportCreteSerializer

        return ReportSerializer
