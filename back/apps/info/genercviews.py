from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.info.serializers import UserListSerializer
from apps.users.models import User
from collections import defaultdict


class ListUsers(ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        filter_queryset = self.filter_rol(serializer)
        return Response(filter_queryset, status=status.HTTP_200_OK)

    def filter_rol(self, serializer):
        new_query = defaultdict(list)
        for row in serializer.data:
            if row.get('is_verified'):
                rol = row.get('rol')
                new_query[rol].append(row)
        return new_query