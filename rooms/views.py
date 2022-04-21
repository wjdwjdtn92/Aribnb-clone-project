from functools import partial
import re
from django.http import HttpResponse
from rooms.models import Room
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RoomSerializer


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
        serializer = RoomSerializer(rooms, many=True)
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = RoomSerializer(data=request.data)
        # print(serializer.validated_data)

        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            room = serializer.save(user=request.user)
            serializer = RoomSerializer(room).data
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

# class ListRoomView(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class RoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        # print(serializer.validated_data)

        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if serializer.is_valid():
            room = serializer.save(user=request.user)
            serializer = RoomSerializer(room).data
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomView(APIView):
    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            return None

    def get(self, request, pk):
        room = self.get_room(pk)

        if room is not None:
            serializer = RoomSerializer(room)
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        room = self.get_room(pk)

        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            serializer = RoomSerializer(room,data=request.data, partial=True)
            
            if serializer.is_valid():
                room = serializer.save()
                serializer = RoomSerializer(room).data
                
                return Response(serializer, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        room = self.get_room(pk)

        if room is not None:
            if room.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            room.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
