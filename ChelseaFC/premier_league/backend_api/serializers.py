from .models import Clubs
from rest_framework import serializers


class clubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = "__all__"


class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ["matches"]
