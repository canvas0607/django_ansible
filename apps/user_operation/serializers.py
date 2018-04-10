from rest_framework import serializers
from .models import UserServerCommandLine


class UserServerCommandLineCreateSerializer(serializers.ModelSerializer):
    # 默认获当前使用用户为创建者

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserServerCommandLine
        fields = ('user','server','command')


class UserServerCommandLineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserServerCommandLine
        fields = "__all__"
