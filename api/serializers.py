from rest_framework import serializers

class RouteRequestSerializer(serializers.Serializer):
    start = serializers.ListField(
        child=serializers.FloatField(),
        min_length=2,
        max_length=2,
        help_text="Starting point [lat, lon]"
    )
    end = serializers.ListField(
        child=serializers.FloatField(),
        min_length=2,
        max_length=2,
        help_text="Destination point [lat, lon]"
    )