# from django.db.transaction import atomic
from rest_framework import serializers

from user.models import User
from palette.models import Palette, Color, ColorInPalette


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "username"
        )


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = "__all__"


class ColorInPaletteSerializer(serializers.ModelSerializer):

    id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source="color"
    )
    name = serializers.SlugRelatedField(
        source="color",
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = ColorInPalette
        fields = "__all__"


class PaletteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Palette
        fields = "__all__"


class PaletteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Palette
        fields = "__all__"
