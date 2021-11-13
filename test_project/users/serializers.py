from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, Announcement


class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    status = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    status = serializers.CharField()
    owner_id = CustomUser.pk
    executor_id = CustomUser.pk

    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        return Announcement.objects.create(**validated_data)


