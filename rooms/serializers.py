from rest_framework import serializers
from .models import Room
from users.serializers import UserSerialzer

class ReadRoomSerializer(serializers.ModelSerializer):
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
        

class WriteRoomSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print(validated_data)
        return Room.objects.create(**validated_data)
    
    class Meta:
        model= Room
        exclude= (
            "user",
        )
    