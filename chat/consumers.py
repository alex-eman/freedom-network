"""
chat/consumers.py
"""

import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Thread, ChatMessage

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })

        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        thread_obj = await self.get_thread(me, other_user)

    async def websocket_receive(self, event):

        front_text = event.get('text', None)
        if front_text is not None:

            # Get entered text
            loaded_dict_data = json.loads(front_text)
            msg = loaded_dict_data.get('message')
            
            # Get user who sent text
            user = self.scope['user']
            username = 'invalid'
            if user.is_authenticated:
                username = user.username

            # Prepare response package
            response = {
                'message': msg,
                'username': username
            }

            # Send the message
            await self.send({
                "type": "websocket.send",
                "text": json.dumps(response)
            })

    async def websocket_disconnect(self, event):
        print("disconnected", event)

    @database_sync_to_async
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]
