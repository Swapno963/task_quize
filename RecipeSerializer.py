from rest_framework import serializers
from .models import Recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "all"