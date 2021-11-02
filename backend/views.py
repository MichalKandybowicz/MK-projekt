from datetime import datetime

from django.db.models import Q
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
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

    def list(self, request):
        today = datetime.today()
        query_set = Attack.objects.filter(entry_time__gt=today)
        serializer = AttackSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True)
    def from_village(self, request, pk):
        today = datetime.today()

        query_set = Attack.objects.filter(
            Q(attacker_cords__cords=pk) &
            Q(entry_time__gt=today)
        )
        serializer = AttackSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)


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

    @action(detail=True)
    def from_village(self, request, pk):
        query_set = Report.objects.filter(attacker_cords__cords=pk)
        serializer = ReportSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data)
