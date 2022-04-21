import re
from django.http import HttpResponse
from rooms.models import Room
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from .serializers import ReadRoomSerializer, WriteRoomSerializer



# Create your views here.


# def list_rooms(request):
#     rooms = Room.objects.all()
#     data = serializers.serialize('json', rooms)

#     response = HttpResponse(content=data)
#     return response

@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = ReadRoomSerializer(rooms, many=True)
        return Response(data=serializer.data)
    
    elif request.method == "POST":
        serializer = WriteRoomSerializer(data=request.data)
        # print(serializer.validated_data)
        
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            serializer = ReadRoomSerializer(room).data
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# class ListRoomView(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
    


class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = ReadRoomSerializer
                       