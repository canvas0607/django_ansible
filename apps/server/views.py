from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import ServerDetailSerializer

from .models import ServerDetail

class ServerDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        获取所有服务器信息
    retrieve:
        获取单个服务器信息
    """
    serializer_class = ServerDetailSerializer
    queryset = ServerDetail.objects.all()

