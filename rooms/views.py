from django.http import HttpResponse
from rooms.models import Room
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import RoomSerializer



# Create your views here.


# def list_rooms(request):
#     rooms = Room.objects.all()
#     data = serializers.serialize('json', rooms)

#     response = HttpResponse(content=data)
#     return response

# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerialzer(rooms, many=True)
#     return Response(data=serialized_rooms.data)

class ListRoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    


class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
                       