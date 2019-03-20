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

        # Get participants of chat room
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']

        # Get unique thread object
        # Name the chat_room uniquely
        thread_obj = await self.get_thread(me, other_user)
        print(me, thread_obj.id)
        chat_room = "thread_{}".format(thread_obj.id)
        self.thread_obj = thread_obj
        self.chat_room = chat_room
        
        # Create the chat room with unique name
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )

        # Connect to the chat room
        await self.send({
            "type": "websocket.accept"
        })

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
                #await self.create_chat_message(user, msg)

            await self.create_chat_message(user, msg)

            # Prepare response package
            response = {
                'message': msg,
                'username': username
            }

            await self.channel_layer.group_send(
                self.chat_room,
                {
                    "type": "chat_message",
                    "message": json.dumps(response)
                }
            )

    async def chat_message(self, event):
        print('message', event)
        await self.send({
            "type": "websocket.send",
            "text": event['message']
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        await self.send({
            "type": "websocket.close"
            })

    @database_sync_to_async
    def get_thread(self, user, other_username):
        return Thread.objects.get_or_new(user, other_username)[0]

    @database_sync_to_async
    def create_chat_message(self, me, msg):
        return ChatMessage.objects.create(thread=self.thread_obj, user=me, message=msg)
