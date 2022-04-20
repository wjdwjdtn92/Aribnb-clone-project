from rest_framework import serializers
from .models import Room
from users.serializers import UserSerialzer

class RoomSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=140)
    # price = serializers.IntegerField()
    # bedrooms = serializers.IntegerField()
    # instant_book = serializers.BooleanField()
    user = UserSerialzer()
    
    class Meta:
        model= Room
        exclude= (
            "modified",
        )