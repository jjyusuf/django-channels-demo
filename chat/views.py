from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html',{
        'room_name': room_name
    })


def send(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("chat_lobby", 
    {
        "type": "chat_message", 
        "message":"Welcome again from else where"
    })
    return render(request, 'chat/send.html')
