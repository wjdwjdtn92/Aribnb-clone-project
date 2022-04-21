from rest_framework import serializers
from .models import Room
from users.serializers import UserSerialzer

# class ReadRoomSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(max_length=140)
#     # price = serializers.IntegerField()
#     # bedrooms = serializers.IntegerField()
#     # instant_book = serializers.BooleanField()
#     user = UserSerialzer()
    
#     class Meta:
#         model= Room
#         exclude= (
#             "modified",
#         )
        

class RoomSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     print(validated_data)
    #     return Room.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.beds = validated_data.get('beds', instance.beds)
    #     instance.lat = validated_data.get('lat', instance.lat)
    #     instance.lng = validated_data.get('lng', instance.lng)
    #     instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
    #     instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
    #     instance.check_in = validated_data.get('check_in', instance.check_in)
    #     instance.check_out = validated_data.get('check_out', instance.check_out)
    #     instance.instant_book = validated_data.get('instant_book', instance.instant_book)
        
    #     instance.save()
    #     return instance
    
    class Meta:
        model= Room
        exclude= ("modified",)
        read_only_fields=("user", "created", "id", "updated",)
    