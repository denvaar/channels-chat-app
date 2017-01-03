from channels.routing import route

channel_routing = [
    route('websocket.receive', 'apps.chat.consumers.ws_echo'),
]
