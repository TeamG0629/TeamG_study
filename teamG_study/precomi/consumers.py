import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import connection
from django.db.utils import OperationalError
from channels.db import database_sync_to_async
from django.core import serializers
from django.utils import timezone
from .models import *
from urllib.parse import urlparse
import datetime
import time
from django.db.models import Max


class ChatConsumer(AsyncWebsocketConsumer):
    groups = ['broadcast']

    async def connect(self):
        # room_id = self.scope["url_route"]["kwargs"]["id"]
        # self.room_group_name = str(room_id)
        await self.accept()
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_r_%s" % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    # Receive message from WebSocket
    async def receive(self, text_data):
        # print(str(text_data))
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Send message to room group
        self.createMessage(text_data_json)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type" : "chat_message",
            "message": message,
        }))
        print(message)


    @database_sync_to_async
    def createMessage(self, event):
        try:
            room = Room.objects.filter(
                id=self.room_group_name
            )
            Message.objects.create(
                room=room,
                name=event['name'],
                content=event['message'],
            )
        except Exception as e:
            raise print(e)
