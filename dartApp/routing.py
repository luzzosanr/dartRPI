from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from memory import consumers

# urls that handles the websocket connection is put here
websocket_urlpatterns=[
    path('ws/chat/', consumers.ChatConsumer),
    ]

application = ProtocolTypeRouter( 
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)