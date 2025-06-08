# serializers.py

from rest_framework import serializers

from .models import Link, Profile


class LinkSerializer(serializers.ModelSerializer):
    # Expose move_up/down as writable actions rather than model fields
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = Link
        fields = [
            "id",
            "title",
            "url",
            "is_active",
            "order",
        ]
        read_only_fields = ["id", "order"]


class ProfileSerializer(serializers.ModelSerializer):
    # Nest links and allow reordering via their own endpoints
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "display_name",
            "bio",
            "avatar",
            "theme",
            "links",
        ]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        # allow partial updates to theme JSON without overwriting
        theme_data = validated_data.pop("theme", None)
        if theme_data is not None:
            # merge incoming theme props into existing JSON
            instance.theme = {**instance.theme, **theme_data}
        # standard fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
