from rest_framework import serializers
from .models import Face


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = "__all__"
