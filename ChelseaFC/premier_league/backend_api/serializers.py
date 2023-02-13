from .models import Clubs
from rest_framework import serializers


class clubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ["id", "name", "short_code",
                  "common_name", "logo", "biography", "trophies"]


class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ["matches"]

class standingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ["standing"]
