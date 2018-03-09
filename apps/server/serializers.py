from rest_framework import serializers
from .models import ServerDetail
class ServerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerDetail
        fields = "__all__"