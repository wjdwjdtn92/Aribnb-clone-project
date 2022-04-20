from rest_framework import serializers
from .models import User

class UserSerialzer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=140)
    # price = serializers.IntegerField()
    # bedrooms = serializers.IntegerField()
    # instant_book = serializers.BooleanField()
    class Meta:
        model= User
        exclude=(
           "groups",
           "user_permissions",
           "password",
           "last_login",
           "is_superuser",
           "is_staff",
           "is_active",
           "date_joined",
           "favs",
        )