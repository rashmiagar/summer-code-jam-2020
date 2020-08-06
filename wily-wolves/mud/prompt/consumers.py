import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from pyfiglet import figlet_format
from django.contrib.auth.models import User
from game.models import Player
from channels.auth import (login as auth_login, logout as auth_logout)
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256
from game.engine import Engine

welcome_text = (figlet_format('Wily Wolves', font='starwars') +
        f"\nThis is the Wily Wolves MUD project for the Python Discord: Summer-code-jam-2020"
        f"\nType 'login' if you already have an account or 'new' to start this journey!")

class MudConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'MUD'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        async_to_sync(auth_logout)(self.scope)

        self.accept()

        self.send(text_data=json.dumps({
            'message': welcome_text
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        command = message.lower().split(maxsplit=1)[0]
        if self.scope['user'].is_authenticated == True:
            try:
                e = Engine(consumer=self, command_line=message)
                message = eval('e.' + command + '()')
            except AttributeError:
                message = f"{command} is not a valid command! Type 'help' if you need."
        elif command == 'login':
            if len(message.split()) == 3:
                username_to_login = message.split()[1]
                plain_password_to_login = message.split()[2]
                if len(User.objects.filter(username=username_to_login)) == 1:
                    self.user = User.objects.get(username=username_to_login)
                    dt = self.user.last_login
                    if django_pbkdf2_sha256.verify(plain_password_to_login, self.user.password) == True:
                        async_to_sync(auth_login)(self.scope, user=self.user)
                        if dt:
                            message = (f"Welcome back, {self.user}! \n" +
                                f"You last logged in at {dt.strftime('%Y-%m-%d %H:%M')} (UTC)")
                        else:
                            message = (f"Welcome to the MUD, {self.user}! \n" +
                                f"Since it's your first time here, we'll guide you in your first steps.")
                        print(f"Successfully logged in as {self.user}")
                        async_to_sync(self.channel_layer.group_send)(
                            self.room_group_name,
                            {
                                'type': 'global_message_not_me',
                                'message': f"{self.user} is back to WilyWolves MUD!",
                                'sender_channel_name': self.channel_name
                            }
                        )
                    else:
                        message = "Wrong password! Please try 'login <username> <password> again."
                else:
                    message = f"{username_to_login!r} is not a valid username. If you are new here, please type 'new'"
            else:
                message = "To log in, please type 'login <username> <password>'."
        elif command == 'new':
            if len(message.split()) == 3:
                username_to_create = message.split()[1]
                password_to_create = message.split()[2]
                hashed_password = make_password(password_to_create)
                if len(User.objects.filter(username=username_to_create)) == 0:
                    new_user = User(username=username_to_create, password=hashed_password, is_superuser=False, is_staff=False)
                    new_user.save()
                    new_player = Player(user_id=new_user)
                    new_player.save()
                else:
                    message = f"Someone is already using {username_to_create}"
            else:
                message = "To create a new user, please type 'new <username> <password>'."
        else:
            message = "You need to log in first. Please type 'login' or 'new'"

        if message != False:
            self.send(text_data=json.dumps({
                'message': message
            }))

    # Types of messages
    def global_message(self, event):
        message = event['message']
        # Send a message to everybody in the MUD room
        self.send(text_data=json.dumps({
            'message': message
        }))

    def global_message_login_required(self, event):
        message = event['message']
        if self.scope['user'].is_authenticated == True:
            # Send a message to everybody in the MUD room
            self.send(text_data=json.dumps({
                'message': message
            }))

    def global_message_not_me(self, event):
        message = event['message']
        # Send a message to everyone else other than the sender
        if self.channel_name != event['sender_channel_name']:
            self.send(text_data=json.dumps({
                    'message': message
        }))

    def message_to_self(self, event):
        message = event['message']
        # Send a message to everyone else other than the sender
        if self.channel_name == event['sender_channel_name']:
            self.send(text_data=json.dumps({
                    'message': message
        }))