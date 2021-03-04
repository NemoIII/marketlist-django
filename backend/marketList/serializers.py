from .models import MarketList
from rest_framework import serializers


class MarketListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MarketList
        fields = ("id", "title", "completed")