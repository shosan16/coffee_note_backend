from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    レシピモデル用のシリアライザ
    """

    class Meta:
        model = Recipe
        fields = [
            "id",
            "name",
            "click_count",
            "click_count",
            "grind_size",
            "coffee_amount",
            "water_amount",
            "description",
        ]
