"""
core/routing.py
"""

from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({

    # Checks core/settings.py ALLOWED_HOSTS
    'websocket': AllowedHostsOriginValidator(
        # Allow user in websocket
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
                ]
            )
        )

    )
    # Empty for now (https -> django vies is added by default)
})
