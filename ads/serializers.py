from rest_framework import serializers

from ads.models import Ad


class AdListSerializer(serializers.ModelSerializers):

    class Meta:
        model = Ad
        fields = "__all__"