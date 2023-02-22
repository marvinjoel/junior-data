from rest_framework import serializers

from apps.info.models import SocialMedia
from apps.users.models import User


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    social = SocialMediaSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'rol', 'avatar', 'social', 'description', 'is_verified']