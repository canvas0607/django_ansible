from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status

from suitable import Api

from .models import UserServerCommandLine
from .serializers import UserServerCommandLineCreateSerializer,UserServerCommandLineListSerializer
from utils.authenticationclass import auth_pattern
from rest_framework.permissions import IsAuthenticated

class UserServerCommandLineViewSet(viewsets.ReadOnlyModelViewSet,mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    list:
        列出用户操作的记录
    retrieve:
        获取当个用户操作记录
    create:
        添加一条命令行数据
    """

    queryset = UserServerCommandLine.objects.all()

    #authentication_classes = auth_pattern
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserServerCommandLineCreateSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return UserServerCommandLineListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        server = data['server']
        command = data['command']

        try:
            api = Api(
                server.ip,
                remote_pass=server.ssh_password,
                remote_user=server.ssh_name,
                extra_vars={"ansible_ssh_port": server.ssh_port}
            )
            command_res = api.command(command).stdout()
            self.perform_create(serializer)
        except Exception as e:
            command_res = e
        data = dict(server=server.id,command=command,command_res = command_res)
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

