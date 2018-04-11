from rest_framework import serializers
from .models import ServerDetail, ServerStatus


class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatus
        fields = "__all__"


class ServerDetailSerializer(serializers.ModelSerializer):
    server_status = ServerStatusSerializer(many=False)
    class Meta:
        model = ServerDetail
        fields = ("server_status","id","ip","name","desc","add_time","server_is_active","ssh_is_active","ssh_error_msg")
